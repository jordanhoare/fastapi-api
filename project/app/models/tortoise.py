# from fileinput import close

# from tortoise import fields, models
# from tortoise.contrib.pydantic import pydantic_model_creator

from tortoise import fields, init_models, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Stock(models.Model):
    """
    This references a Stock
    """

    id = fields.IntField(pk=True)
    symbol = fields.CharField(max_length=20, unique=True, null=False)
    company = fields.CharField(max_length=50, null=False)
    stock_prices: fields.ReverseRelation["Stock_Price"]


class Stock_Price(models.Model):
    """
    This references a Stock_Price in a Stock
    """

    id = fields.IntField(pk=True)
    stock_id = fields.IntField(null=False)
    date = fields.DatetimeField(null=False)
    open = fields.FloatField(null=False)
    high = fields.FloatField(null=False)
    open = fields.FloatField(null=False)
    close = fields.FloatField(null=False)
    adjusted_close = fields.FloatField(null=False)
    volume = fields.IntField(null=False)

    stock = fields.ForeignKeyField(
        "models.Stock",
        related_name="stock_prices",
        description="The stock this describe",
    )


# Tortoise.init_models(["__main__"], "models")
Stock_Pydantic = pydantic_model_creator(Stock)
Stock_Price_Pydantic = pydantic_model_creator(Stock_Price)


# from tortoise import fields, models
# from tortoise.contrib.pydantic import pydantic_model_creator


# class TextSummary(models.Model):
#     """
#     Define a new database model called TextSummary.
#     """

#     url = fields.TextField()
#     summary = fields.TextField()
#     created_at = fields.DatetimeField(auto_now_add=True)

#     def __str__(self):
#         return self.url

# Tortoise.init_models(["__main__"], "models")
# SummarySchema = pydantic_model_creator(TextSummary)
