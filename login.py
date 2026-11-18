import streamlit as st
import mysql.connector
from database import connect_db
from password_security import verify_password

st.set_page_config(
    page_title="Login - Kafe Nusantara",
    page_icon="☕",
    layout="centered",
)

menu_page = st.Page("app.py", title="Menu Kafe")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
  --cream: #fffaf3;
  --coffee: #3f2a20;
  --caramel: #c98558;
  --gold: #daa76f;
}

html, body, [class*="css"] {
  font-family: "Plus Jakarta Sans", sans-serif;
}

.stApp {
  background:
    radial-gradient(circle at 12% 18%, rgba(218, 167, 111, .22), transparent 22rem),
    radial-gradient(circle at 88% 82%, rgba(201, 133, 88, .18), transparent 24rem),
    linear-gradient(135deg, #f8efe3 0%, #fffaf5 48%, #ead7c1 100%);
}

[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] { display: none; }
.block-container {
  max-width: 980px !important;
  padding-top: 8vh !important;
  padding-bottom: 5vh !important;
}

.login-shell {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 560px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,.85);
  border-radius: 32px;
  background: rgba(255,255,255,.72);
  box-shadow: 0 28px 80px rgba(91, 61, 43, .16);
  backdrop-filter: blur(18px);
  animation: shellIn .75s cubic-bezier(.2,.75,.25,1) both;
}

.brand-panel {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 52px 48px;
  color: white;
  background:
    linear-gradient(145deg, rgba(63,42,32,.82), rgba(126,79,54,.92)),
    url("https://images.unsplash.com/photo-1445116572660-236099ec97a0?auto=format&fit=crop&w=900&q=80") center/cover;
  overflow: hidden;
}

.brand-panel::after {
  content: "";
  position: absolute;
  width: 260px;
  height: 260px;
  right: -130px;
  bottom: -130px;
  border: 1px solid rgba(255,255,255,.25);
  border-radius: 50%;
  box-shadow: 0 0 0 40px rgba(255,255,255,.04), 0 0 0 80px rgba(255,255,255,.03);
  animation: orbit 10s linear infinite;
}

.brand-mark {
  display: inline-flex;
  width: 64px;
  height: 64px;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255,255,255,.35);
  border-radius: 20px;
  background: rgba(255,255,255,.12);
  font-size: 32px;
  box-shadow: 0 12px 30px rgba(0,0,0,.12);
  animation: float 3.2s ease-in-out infinite;
}

.brand-copy h1 {
  margin: 18px 0 10px;
  color: white;
  font-size: 38px;
  line-height: 1.05;
  letter-spacing: -2px;
}

.brand-copy p {
  max-width: 330px;
  color: rgba(255,255,255,.78);
  font-size: 15px;
  line-height: 1.7;
}

.form-panel {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 52px;
  animation: formIn .75s .18s cubic-bezier(.2,.75,.25,1) both;
}

.form-kicker {
  margin-bottom: 8px;
  color: var(--caramel);
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 2.2px;
  text-transform: uppercase;
}

.form-panel h2 {
  margin: 0 0 8px;
  color: var(--coffee);
  font-size: 32px;
  letter-spacing: -1.5px;
}

.form-subtitle {
  margin: 0 0 28px;
  color: #907d70;
  font-size: 14px;
}

.stTextInput label {
  color: #674f40;
  font-size: 13px;
  font-weight: 700;
}

.stTextInput input {
  height: 52px;
  border: 1px solid #eadfd3;
  border-radius: 14px;
  background: rgba(255,255,255,.85);
  color: var(--coffee);
  transition: all .25s ease;
}

.stTextInput input:focus {
  border-color: var(--caramel);
  box-shadow: 0 0 0 4px rgba(201,133,88,.12);
}

.stButton button {
  width: 100%;
  height: 54px;
  border: 0;
  border-radius: 14px;
  background: linear-gradient(135deg, #4b3327, #c98558);
  color: white;
  font-weight: 800;
  letter-spacing: .2px;
  box-shadow: 0 14px 28px rgba(151, 96, 61, .24);
  transition: transform .2s ease, box-shadow .2s ease;
}

.stButton button:hover {
  transform: translateY(-3px);
  box-shadow: 0 18px 34px rgba(151, 96, 61, .32);
  color: white;
}

.stButton button:active { transform: translateY(0); }

[data-testid="stVerticalBlockBorderWrapper"] {
  overflow: hidden;
  border: 1px solid rgba(255,255,255,.85) !important;
  border-radius: 32px;
  background: rgba(255,255,255,.72);
  box-shadow: 0 28px 80px rgba(91,61,43,.16);
  backdrop-filter: blur(18px);
  animation: shellIn .75s cubic-bezier(.2,.75,.25,1) both;
}

[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlock"] {
  align-items: stretch;
}

[data-testid="stAlert"] {
  border: 0;
  border-radius: 12px;
  margin-top: 12px;
  animation: formIn .35s ease both;
}

@keyframes shellIn {
  from { opacity: 0; transform: translateY(28px) scale(.98); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes formIn {
  from { opacity: 0; transform: translateY(12px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes float {
  0%, 100% { transform: translateY(0) rotate(-2deg); }
  50% { transform: translateY(-9px) rotate(2deg); }
}
@keyframes orbit { to { transform: rotate(360deg); } }

@media (max-width: 760px) {
  .block-container { padding: 24px 14px !important; }
  .login-shell { grid-template-columns: 1fr; }
  .brand-panel { min-height: 220px; padding: 32px; }
  .brand-copy h1 { font-size: 30px; }
  .brand-copy p { display: none; }
  .form-panel { padding: 36px 28px; }
}
</style>
""", unsafe_allow_html=True)

def login_view():
    with st.container(border=True):
        brand_col, form_col = st.columns([1, 1], gap="large")

        with brand_col:
            st.markdown("""
      <section class="brand-panel">
        <div class="brand-mark">☕</div>
        <div class="brand-copy">
          <h1>Kafe<br>Nusantara</h1>
          <p>Ruang hangat untuk menikmati racikan terbaik dan mengelola menu favorit setiap hari.</p>
        </div>
      </section>
            """, unsafe_allow_html=True)

        with form_col:
            st.markdown("""
      <section class="form-panel">
        <div class="form-kicker">Welcome back</div>
        <h2>Masuk Akun</h2>
        <p class="form-subtitle">Silakan masuk untuk mengakses dashboard menu.</p>
            """, unsafe_allow_html=True)
            username = st.text_input("Username", placeholder="Masukkan username")
            password = st.text_input("Password", type="password", placeholder="Masukkan password")

            if st.button("Masuk ke Dashboard", use_container_width=True):
                if not username.strip() or not password:
                    st.error("Username dan password wajib diisi.")
                else:
                    try:
                        db = connect_db()
                        try:
                            cursor = db.cursor()
                            try:
                                cursor.execute(
                                    "SELECT password FROM users "
                                    "WHERE username = %s LIMIT 1",
                                    (username.strip(),),
                                )
                                user = cursor.fetchone()
                            finally:
                                cursor.close()
                        finally:
                            db.close()

                        if user and verify_password(password, user[0]):
                            st.session_state["authenticated"] = True
                            st.session_state["username"] = username.strip()
                            st.switch_page(menu_page)
                        else:
                            st.error("Username atau Password Salah!")
                    except mysql.connector.Error as exc:
                        st.error(f"Tidak dapat terhubung ke database: {exc}")

            st.markdown("</section>", unsafe_allow_html=True)


navigation = st.navigation(
    [
        st.Page(login_view, title="Login"),
        menu_page,
    ],
    position="hidden",
)
navigation.run()