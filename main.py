import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage  # Resim eklemek için PhotoImage kullanılır
from PIL import Image, ImageTk
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.hash import sha256_crypt

# SQLite veritabanı oluşturma
engine = create_engine('sqlite:///user.db', echo=False)
Base = declarative_base()

# Kullanıcı bilgilerini temsil eden veritabanı tablosu
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True) 
    username = Column(String, unique=True) # eşsiz
    password = Column(String)

Base.metadata.create_all(engine)

# Tkinter uygulaması oluşturma
app = tk.Tk()
app.title("Login")
app.geometry("1000x600")

# Arka plan resmini eklemek için ImageTk kullanımı
bg_image = Image.open("images/bg1.png")  # Arka plan resmi dosyasının adını ve yolunu belirtin
bg_image = bg_image.resize((1000, 600), Image.ANTIALIAS)  # Resmi pencere boyutuna uygun olarak yeniden boyutlandırın
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(app, image=bg_image)
bg_label.place(relwidth=1, relheight=1)



