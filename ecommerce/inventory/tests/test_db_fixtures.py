#Using a database ot refelect data 
import pytest
from ecommerce.inventory import models

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)

def test_inventory_category_dbfixture(
    db, db_fixture_setup, id, name, slug, is_active
    #data fixtures
):
    result=models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active

@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("fashion", 1),
        ("trainers", 1),
        ("baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(
db, category_factory, slug, is_active
):
    result = category_factory.create(slug=slug, is_active=is_active)
    print(result.name)
    assert result.slug == slug
    assert result.is_active == is_active

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (
            1,
            "45425810",
            "widstar running sneakers",
            "widstar-running-sneakers",
            "This is just something i will just put as an input here, sorry if i incovenienced you",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            "45434425",
            "impact puse dance shoe",
            "impact-puse-dance-shoe",
            "This is just something i will just put again as an input here, sorry if i incovenienced you",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_product_dbfixture(
    db,
    db_fixture_setup,
    id, 
    web_id, 
    name, 
    slug, 
    description, 
    is_active, 
    created_at, 
    updated_at,
    ):
        result = models.Product.objects.get(id=id)
        result_create_at= result.created_at.strftime("%Y-%m-%d %H:%M:%S")
        result_updated_at= result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        assert result.web_id == web_id
        assert result.name == name
        assert result.slug == slug
        assert result.description == description
        assert result.is_active == is_active
        assert result_create_at == created_at
        assert result_updated_at == updated_at

def test_inventory_db_product_uniqueness_integrity(db, product_factory):
    new_web_id = product_factory.create(web_id = 123456789)
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456789)

@pytest.mark.dbfixture
def test_inventory_db_product_insert_data(
    db, product_factory, category_factory
):
    new_category = category_factory.create()
    new_product = product_factory.create(category=(1, 36))
    result_product_category = new_product.category.all().count()

    assert "web_id_" in new_product.web_id
    assert result_product_category == 2
    