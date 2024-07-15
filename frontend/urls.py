
from django.urls import path
from frontend import views
from django.contrib.auth import views as auth_views



app_name = 'frontend'


urlpatterns = [
    path('one/<int:pst>/', views.one, name='one'),
    path('two/<int:pst>/', views.two, name='two'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('activateEmail', views.activateEmail, name='activateEmail'),
    path('register', views.register, name='register'),
    path('login', views.custom_login, name='custom_login'),
    path('logout', views.custom_logout, name='logout'),
    path('confirm_logout', views.confirm_logout, name='confirm_logout'),
    path('edit-profile', views.edit_profile, name='edit_profile'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    path('news', views.news, name='news'),
    path('homeshop', views.homeshop, name='homeshop'),
    path('info', views.info, name='info'),
    path('like_post/<int:pk>/', views.like_post, name='like_post'),
    path('base', views.base, name='base'),
    path('profile', views.profile, name='profile'),
    path('category', views.category, name='category'),
    path('product-shop', views.shop, name='shop'),
    path('categorydetail/<int:id>', views.categorydetail, name='categorydetail'),
    #     PRODUCT CODE ENDS HERE
    path('add-post', views.add_post, name='add_post'),
    path('view-post', views.view_post, name='view_post'),
    path('delete_post/<int:pst_id>', views.delete_post, name='delete_post'),
    path('edit_post/<int:pst_id>', views.edit_post, name='edit_post'),
    path('favourite_post/<int:id>/', views.favourite_post, name='favourite_post'),
     path('post-list', views.post_list, name='post_list'),
     #path('error_404_view', views.error_404_view, name='error_404_view'),
     path('about', views.about, name='about'),
     path('privacy_policy', views.privacy_policy, name='privacy_policy'),
     path('contact', views.contact, name='contact'),
     path('newsletter', views.newsletter, name='newsletter'),
     path('add_video', views.add_video, name='add_video'),
     path('show_video', views.show_video, name='show_video'),
     path('view_video/<int:id>/', views.view_video, name='view_video'),






#     PRODUCT CODE ENDS HERE
    # CART STATRT HERE    
     path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail, name='cart_detail'),
     path('checkout',views.checkout, name='checkout'),
     path('tracking',views.tracking, name='tracking'),
     path('delete_tracking/<int:id>/', views.delete_tracking, name='delete_tracking'),
     path('view_order/<int:id>/', views.view_order, name='view_order'),
    
    
    
    # CART END HERE

    #SEARCH BAR CODE
    path('search', views.search, name='search')

    
    




    ]
    
