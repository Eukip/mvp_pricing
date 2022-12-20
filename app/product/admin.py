from django.contrib import admin
from .models import Category, SubCategory, SubSubCategory, RoleProduct, Competitor, Product, StrategyProduct, CompetitorProduct, AnalogProduct, FileModel


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(SubCategory, SubCategoryAdmin)


class SubSubCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(SubSubCategory, SubSubCategoryAdmin)


class RoleProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(RoleProduct, RoleProductAdmin)


class CompetitorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Competitor, CompetitorAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)


class StrategyProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(StrategyProduct, StrategyProductAdmin)


class CompetitorProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(CompetitorProduct, CompetitorProductAdmin)


class AnalogProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(AnalogProduct, AnalogProductAdmin)


class FileModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(FileModel, ProductAdmin)