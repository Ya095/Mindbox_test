from pyspark.sql import SparkSession


# создание сессии
spark = SparkSession.builder.appName("task_2").getOrCreate()

# создание таблицы категорий
cats_table = spark.createDataFrame([
    (1, "Еда"),
    (2, "Одежда"),
    (3, "Техника"),
    (4, "Красота и уход"),
    (5, "Спорт")],
    ["id", "Категория"],
)

# создание таблицы продуктов
products_table = spark.createDataFrame([
    (1, "Молоко"),
    (2, "Футболка"),
    (3, "Смартфон"),
    (4, "Шампунь"),
    (5, "Беговая дорожка"),
    (6, "Стол"),
    (7, "Телевизор"),
    (8, "Лак для ногтей"),
    (9, "Велосипед"),
    (10, "Маска для лица"),
    (11, "Шапка"),
    (12, "Кондиционер"),
    (13, "Слойка")],
    ["id", "Товар"]
)

# таблица пересечений (категория - продукт)
cats_and_products_table = spark.createDataFrame([
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (3, 7),
    (4, 8),
    (5, 9),
    (4, 10),
    (2, 11),
    (3, 12),
    (1, 13)],
    ["cat_id", "product_id"]
)

df_result = (
    products_table.join(
        cats_and_products_table,
        products_table.id == cats_and_products_table.product_id,
        how='left'
    )
    .join(cats_table, cats_and_products_table.cat_id == cats_table.id, how='left')
    .select(['Категория', 'Товар'])
)

df_result.orderBy("cat_id").show(truncate=True)
