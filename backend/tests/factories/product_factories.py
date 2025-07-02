import factory
from product.models import Product, Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('pystr')
    
    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    id = factory.Sequence(lambda n: n + 1)
    title = factory.Faker('pystr')
    description = factory.Faker('pystr')
    price = factory.Faker('pyint')
    
    class Meta:
        model = Product
        
    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.categories.add(category)
