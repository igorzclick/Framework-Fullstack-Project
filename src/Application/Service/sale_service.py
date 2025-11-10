from datetime import datetime, timedelta
from src.Infrastructure.Model.sale_model import Sale
from src.Infrastructure.Model.product_model import Product
from src.config.data_base import db

class SaleService:
    @staticmethod
    def create_sale(sale):
        try:
            product = Product.query.filter_by(id=sale.product_id).first()
            if not product:
                return None, "Product not found"
            
            if int(sale.quantity) > int(product.quantity):
                return None, f"Insufficient quantity. Available: {product.quantity}, Requested: {sale.quantity}"
            
            sale.price = product.price * sale.quantity
            
            product.quantity -= sale.quantity
            
            if product.quantity == 0:
                product.status = "Inativo"

            sale.price = product.price * sale.quantity
            
            new_sale = Sale(
                seller_id=sale.seller_id,
                product_id=sale.product_id,
                quantity=sale.quantity,
                price=sale.price
            )
            
            db.session.add(new_sale)
            db.session.commit()
            return new_sale, None
            
        except Exception as e:
            db.session.rollback()
            return None, str(e)

    @staticmethod
    def get_all_sales(period='all'):
        try:
            query = Sale.query
            
            if period != 'all':
                from datetime import datetime, timedelta
                now = datetime.now()
                
                if period == 'today':
                    start_date = datetime(now.year, now.month, now.day)
                    end_date = start_date + timedelta(days=1)
                elif period == 'week':
                    start_date = datetime.now() - timedelta(days=7)
                    end_date = datetime.now()
                elif period == 'month':
                    start_date = datetime(now.year, now.month, 1)
                    end_date = datetime.now()
                else:
                    return []
                
                query = query.filter(Sale.created_at >= start_date, Sale.created_at < end_date)
            
            sales = query.all()
            return [sale.to_dict() for sale in sales]
        except Exception as e:
            return None
        
    @staticmethod
    def get_sale_by_id(sale_id):
        try:
            sale = Sale.query.filter_by(id=sale_id).first()
            return sale.to_dict()
        except Exception as e:
            return None
        
        
    @staticmethod
    def update_sale(sale_id, sale_domain):
        sale = Sale.query.get(sale_id)
        if not sale:
            return None, "Sale not found"

        try:
            sale.product_id = sale_domain.product_id
            sale.quantity = sale_domain.quantity
            sale.price = sale_domain.price

            db.session.commit()
            return sale, None 
        except Exception as e:
            db.session.rollback()
            return None, str(e)

    @staticmethod
    def delete_sale(sale_id):
        try:
            sale = Sale.query.filter_by(id=sale_id).first()

            if not sale:
                return None, "Sale not found"

            db.session.delete(sale)
            db.session.commit()
            return True, "Sale deleted successfully"
        except Exception as e:
            db.session.rollback()
            return None

    @staticmethod
    def get_top_selling_products(limit: int = 5):
        try:
            results = (
                db.session.query(
                    Product,
                    db.func.sum(Sale.quantity).label("total_sold"),
                    db.func.sum(Sale.price).label("total_revenue")
                )
                .join(Sale, Sale.product_id == Product.id)
                .group_by(Product.id)
                .order_by(db.desc("total_sold"))
                .limit(limit)
                .all()
            )
            top_products = []
            for product, total_sold, total_revenue in results:
                data = product.to_dict()
                data["total_sold"] = int(total_sold or 0)
                data["revenue"] = float(total_revenue or 0)
                top_products.append(data)
            return top_products
        except Exception:
            return []

    @staticmethod
    def sum_sales_between(start_dt: datetime, end_dt: datetime):
        total = (
            db.session.query(db.func.coalesce(db.func.sum(Sale.price), 0.0))
            .filter(Sale.created_at >= start_dt, Sale.created_at < end_dt)
            .scalar()
        )
        return float(total or 0.0)

    @staticmethod
    def sum_items_between(start_dt: datetime, end_dt: datetime):
        total = (
            db.session.query(db.func.coalesce(db.func.sum(Sale.quantity), 0))
            .filter(Sale.created_at >= start_dt, Sale.created_at < end_dt)
            .scalar()
        )
        return int(total or 0)

    @staticmethod
    def get_sales_summary():
        now = datetime.now()
        start_today = datetime(now.year, now.month, now.day)
        start_yesterday = start_today - timedelta(days=1)
        start_week = start_today - timedelta(days=7)
        end_today = start_today + timedelta(days=1)

        revenue_today = SaleService.sum_sales_between(start_today, end_today)
        revenue_yesterday = SaleService.sum_sales_between(start_yesterday, start_today)
        revenue_week = SaleService.sum_sales_between(start_week, end_today)
        
        items_today = SaleService.sum_items_between(start_today, end_today)
        items_yesterday = SaleService.sum_items_between(start_yesterday, start_today)
        items_week = SaleService.sum_items_between(start_week, end_today)

        return {
            "revenue_today": revenue_today,
            "revenue_yesterday": revenue_yesterday,
            "revenue_week": revenue_week,
            "items_today": items_today,
            "items_yesterday": items_yesterday,
            "items_week": items_week
        }

    @staticmethod
    def get_dashboard_metrics():
        now = datetime.now()
        start_today = datetime(now.year, now.month, now.day)
        end_today = start_today + timedelta(days=1)
        start_month = datetime(now.year, now.month, 1)

        all_time_revenue = (
            db.session.query(db.func.coalesce(db.func.sum(Sale.price), 0.0)).scalar()
        )
        revenue_today = SaleService.sum_sales_between(start_today, end_today)
        revenue_month = SaleService.sum_sales_between(start_month, end_today)

        return {
            "balance": float(all_time_revenue or 0.0),
            "revenue_today": revenue_today,
            "revenue_month": revenue_month
        }