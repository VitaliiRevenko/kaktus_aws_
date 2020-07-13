from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)

    @property
    def child(self):
        return Category.objects.filter(parent_category=self).order_by("name")

    @property
    def has_child(self):
        return self.child.exists()


    @property
    def products(self):
        return Product.objects.filter(category=self)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    old_price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    short_decription = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    @property
    def images(self):
        return Picture.objects.filter(product=self)
    @property
    def first_image(self):
        return self.images.first()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

class Picture(models.Model):
    path = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __repr__(self):
        return self.path.name

    def __str__(self):
        return self.__repr__()

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

class Article(models.Model):
    name = models.CharField(max_length=255)
    descrption = models.TextField()
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

class ArticlePicture(models.Model):
    path = models.ImageField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Page(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

class Oders(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    tel_number = models.CharField(max_length=50)
    comment = models.TextField()
    comment_admin = models.TextField()
    STATUS_LIST = [(0, 'New'),(1, 'Confim'), (2, 'Canceled'), (3, 'Payed'), (4, 'Delivered')]
    status = models.IntegerField(choices=STATUS_LIST, default=0)


class OrderProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=15, decimal_places=2)

class Baner(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.CharField(max_length=250)
    picture = models.ImageField()




# Create your models here.
