CREATE or REPLACE TABLE SLEEKMART_OMS.TRAINING.profit_uk
as (
    SELECT 
    sales_date, SUM() as total_re,
)