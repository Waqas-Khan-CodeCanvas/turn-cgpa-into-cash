

<h1 align="center"> Placement Package Predictor</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/scikit--learn-ML-orange?style=for-the-badge&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" />
  <img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=black" />
</p>
<p align="center">A minimal CGPA → Salary prediction app built with Flask + scikit-learn.</p>

---

## 🚀 Live Deployment

Click below to use the app:

🔗 **https://placement-predictor-production.up.railway.app/**

[![Live App](https://img.shields.io/badge/Railway-Live%20App-success?style=flat-square)](https://placement-predictor-production.up.railway.app/)

---

---

##  Features
- Predicts placement package (LPA) from CGPA  
- Fast, single-page UI  
- Clean Bootstrap 5 layout  
- Chart.js visual trends  
- Confetti animation on prediction  

---

##  Setup

```bash
git clone https://github.com/YOUR_NAME/placement_predictor.git
cd placement_predictor

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py

Open: http://127.0.0.1:5000

```
##  Project Structure
```bash
placement_predictor/
├── app.py                   # Flask routes (home + academic pages)
├── requirements.txt
├── render.yaml
├── placement.csv            # training data
├── model.pkl / scaler.pkl   # auto-generated
├── templates/
│   ├── index.html           # predictor calculator
│   ├── abstract.html        # project summary
│   ├── methodology.html     # data & model flow
│   └── conclusion.html      # results + future work
└── static/
    ├── style.css            # dark theme + confetti
    └── demo1.png / demo2.png

```
## Tech Stack
 - **Backend**: Flask, scikit-learn, pandas
 - **Frontend**: Bootstrap 5, Chart.js, vanilla JS, CSS    animations
 - **Hosting**: `Render`


## Customize

 - Change theme colors → `static/style.css`
 - Swap fonts →` index.html`
 - Replace dataset → add new `placement.csv`  

## Contribute
 - PRs welcome!
 - Found a bug? Open an issue or ping me on <a href="">Twitter</a> or <a href="">linkedin</a>



---

##  Let's Connect

<div align="center" style="display:flex; gap:10px;">
  <a href="https://github.com/YOUR_USERNAME" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-0d1117?style=for-the-badge&logo=github&logoColor=white" />
  </a>

  <a href="https://www.linkedin.com/in/YOUR_USERNAME" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>

  <a href="mailto:YOUR_EMAIL" target="_blank">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>

  <a href="https://twitter.com/YOUR_USERNAME" target="_blank">
    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" />
  </a>
</div>




<p align="center">Made with ❤️ and Flask · MIT License</p>


