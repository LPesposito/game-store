from django.db import models
from product.models.product import Product

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='product_images/')
    is_cover = models.BooleanField(default=False)  # Se é capa
    alt_text = models.CharField(max_length=255, blank=True)  # Descrição da imagem (acessibilidade)

    def __str__(self):
        return f"Image for {self.product.title} {'(Cover)' if self.is_cover else ''}"    