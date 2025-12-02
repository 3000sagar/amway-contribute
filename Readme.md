# 🌐 Amway Contribute — Premium Product Gallery  
A modern, Gen-Z inspired Django web application designed to explore, browse, and download Amway product visuals with a next-gen interactive UI.

---

## 🚀 Features

### ⭐ Gen-Z Inspired UI/UX
- Neon gradients  
- Particle animations  
- Blur layers  
- Floating hero banners  
- Premium product cards  

### ⭐ Product Management
- Categories  
- Brands  
- Product details  
- Multi-image product gallery  
- Fullscreen viewer with download/share  
- Highlight functionality  

### ⭐ Interactive Media Experience
- Floating ticker slider with momentum physics  
- Auto-scrolling product rail  
- Hover-activated share icons  
- Swipe & drag support  

### ⭐ Fully Responsive
- Mobile-first  
- Desktop-optimized  
- Dark mode ready  

---

## 📂 Project Structure

---amway_project/
│── categories/
│── gallery/
│── brands/
│── templates/
│── static/
│── media/ # Ignored on GitHub
│── amway_project/
│── manage.py
│── README.md
│── .gitignore

## 🛠 Tech Stack

- **Backend:** Django 5  
- **Frontend:** Tailwind CSS, Vanilla JS  
- **UI Libraries:** Swiper.js, FontAwesome  
- **Image Handling:** Django FileStorage  
- **Animations:** CSS keyframes + JS  

---

## 🔧 Installation

```bash
git clone https://github.com/sagarrrrrrrr/amway-contribute.git
cd amway-contribute

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
