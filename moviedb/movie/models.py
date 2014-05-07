from django.db import models


class Movie(models.Model):
    api_id = models.BigIntegerField(null=True, default=None)
    imdb_id = models.BigIntegerField(null=True)
    title = models.TextField(null=False)
    release_year = models.DateField(null=True)
    synopsy = models.TextField(null=True)
    rating = models.FloatField(null=False, default=0)
    poster = models.TextField(null=True)
    additional_content = models.TextField(null=True)
    movie_internal_order = models.PositiveIntegerField(null=False, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("MovieCategory")
    actors = models.ManyToManyField("MovieActor")

    def hasStockType(self, stockcode):
        stocks = self.moviestocks.all()
        hasstocktype = False
        stock = MovieStock()
        for stock in stocks:
            if stock.moviestocktype.code == stockcode:
                hasstocktype = True
        return hasstocktype


class MovieOld(models.Model):
    movie = models.OneToOneField(Movie, primary_key=True)
    old_id = models.BigIntegerField()


class MovieActor(models.Model):
    name = models.TextField(null=False)
    #movie = models.ManyToManyField(Movie)


class MovieCategory(models.Model):
    name = models.TextField(null=False)
    #movie = models.ManyToManyField(Movie)


class MovieTrailer(models.Model):
    url = models.URLField(null=False)
    movie = models.ForeignKey(Movie)


class MovieStockType(models.Model):
    code = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=510, null=False)


class MovieStock(models.Model):
    moviestocktype = models.ForeignKey(MovieStockType)
    movie = models.ForeignKey(Movie, related_name="moviestocks")
    original = models.BooleanField(default=True, null=False)
    quantity = models.PositiveSmallIntegerField(default=0, null=False)
    location = models.CharField(null=True, max_length=255)


class MovieRented(models.Model):
    moviestock = models.ForeignKey(MovieStock)
    renter = models.TextField(null=False)
    renterEmail = models.EmailField(null=True)
    note = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


