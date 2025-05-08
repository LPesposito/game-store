import factory

from django.contrib.auth.models import User
from order.models import Order
from django.db.models import Sum

class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('email')
    username = factory.Faker('user_name')
    
    
    class Meta:
        model = User

class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    
    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for product in extracted:
                self.products.add(product)
        
        self.total = self.products.aggregate(Sum('price'))['price__sum'] if self.products.exists() else 0        
    
    
    
    class Meta:
        model = Order
    