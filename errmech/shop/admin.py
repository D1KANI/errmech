from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class CompanySwitchesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class SwitchAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_fk', 'title', 'price', 'color')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class ItemCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_fk', 'title', 'content')
    list_display_links = ('id', 'title')
    # search_fields = ('title',)


class ItemWithPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_fk', 'photo')
    list_display_links = ('id', 'photo')
    # search_fields = ('item_',)


class KeyboardSwitchesAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_fk', 'switch_fk', 'count')
    list_display_links = ('id',)
    list_editable = ('count',)
    # search_fields = ('item_',)


class ItemAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Item
        fields = '__all__'


class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = ('id', 'category_fk', 'company_fk', 'name', 'price', 'get_photo', 'created_at', 'views')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('price',)
    list_filter = ('category_fk', 'company_fk')
    prepopulated_fields = {'slug': ('company_fk', 'name',)}
    fields = (
        'category_fk', 'company_fk', 'name', 'slug', 'desc_small', 'desc', 'price', 'main_photo', 'get_photo',
        'created_at', 'updated_at', 'views',)
    readonly_fields = ('views', 'updated_at', 'created_at', 'get_photo')
    save_on_top = True

    def get_photo(self, obj):
        if obj.main_photo:
            return mark_safe(f'<img src="{obj.main_photo.url}" width="50px">')
        else:
            return '-'

    get_photo.short_description = 'Фото'


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Item
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'short_desc', 'created_at')
    list_display_links = ('id', 'title')
    save_on_top = True


admin.site.register(Company, CompanyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CompanySwitches, CompanySwitchesAdmin)
admin.site.register(Switch, SwitchAdmin)
admin.site.register(KeyboardSwitches, KeyboardSwitchesAdmin)
admin.site.register(ItemWithPhoto, ItemWithPhotoAdmin)
admin.site.register(ItemCharacteristic, ItemCharacteristicAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(News, NewsAdmin)
