import streamlit as st
import pandas as pd
import os

# ==========================================
# 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS CSS
# ==========================================
st.set_page_config(
    page_title="SoniQra | Curaduría Humana de Música",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def inject_custom_css():
    st.markdown("""
    <style>
    .stApp {
        background-color: #121518;
        color: #E2E8F0;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .soniqra-card {
        background-color: #1A1D20;
        border: 1px solid #2A2E33;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .soniqra-card:hover {
        transform: translateY(-4px);
        border-color: #FF5722;
    }
    .badge-accent {
        background-color: rgba(255, 87, 34, 0.15);
        color: #FF5722;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }
    .badge-mint {
        background-color: rgba(0, 230, 195, 0.15);
        color: #00E6C3;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }
    .hero-container {
        text-align: center;
        padding: 40px 20px 20px 20px;
        background: radial-gradient(circle at center, rgba(255, 87, 34, 0.08) 0%, rgba(18, 21, 24, 0) 70%);
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FFFFFF, #E2E8F0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        color: #00E6C3;
        letter-spacing: 2px;
        font-size: 0.95rem;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 20px;
    }
    .brand-logo {
        font-size: 2rem;
        font-weight: 900;
        color: #FF5722;
        letter-spacing: -1px;
    }
    .brand-logo span {
        color: #00E6C3;
    }
    .form-container {
        border: 2px dashed #00E6C3;
        background-color: #1A1D20;
        border-radius: 20px;
        padding: 30px;
        margin-top: 40px;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #121518 !important;
        color: #FFFFFF !important;
        border: 1px solid #2A2E33 !important;
        border-radius: 10px !important;
    }
    div.stButton > button {
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. CARGA Y GESTIÓN DE DATOS (CSV)
# ==========================================
CURADORES_FILE = "curadores.csv"
MIXES_FILE = "mixes.csv"

def init_data():
    df_curadores = pd.DataFrame([
        {
            "id_curador": 1,
            "nombre": "Paulo Forter",
            "usuario": "@Paulo_Mix",
            "genero": "Rock & Alternativo / Indie",
            "seguidores": 1420,
            "icono_url_o_emoji": "🎸",
            "descripcion": "Guitarras chidas, Franz Ferdinand y Foo Fighters para mantener el flow y no dormirte con la tarea."
        },
        {
            "id_curador": 2,
            "nombre": "Ana Valeria",
            "usuario": "@Anna_LoFi",
            "genero": "Estudio & Relax / Lo-Fi",
            "seguidores": 3890,
            "icono_url_o_emoji": "🎧",
            "descripcion": "Beats tranquilos, Jinsang y Nujabes para estudiar sin distracciones y con mucha paz."
        },
        {
            "id_curador": 3,
            "nombre": "Pop Perfection",
            "usuario": "@Pop_Perfection",
            "genero": "Pop & Moderno / Synth-Glow",
            "seguidores": 2980,
            "icono_url_o_emoji": "💖",
            "descripcion": "Sabrina Carpenter, Taylor Swift y los mejores beats pop para cantar a todo volumen."
        },
        {
            "id_curador": 4,
            "nombre": "Gym Beast",
            "usuario": "@Gym_Beast",
            "genero": "Energía & Gym / Phonk",
            "seguidores": 4120,
            "icono_url_o_emoji": "🏋️",
            "descripcion": "Phonk pesado, Gojira y bajos extremos para levantar más pesado en el entrenamiento."
        },
        {
            "id_curador": 5,
            "nombre": "Retro Vibes",
            "usuario": "@Retro_Vibes",
            "genero": "Nocturno & Driving / Synthwave",
            "seguidores": 1850,
            "icono_url_o_emoji": "📻",
            "descripcion": "M83, Kavinsky y sintetizadores ochenteros ideales para manejar de noche."
        }
    ])
    df_curadores.to_csv(CURADORES_FILE, index=False)

    df_mixes = pd.DataFrame([
        # @Pop_Perfection
        {
            "id_mix": 1,
            "usuario_curador": "@Pop_Perfection",
            "titulo_mix": "Pop & Synth-Glow",
            "nombre_cancion": "Espresso - Sabrina Carpenter",
            "descripcion_cancion": "Ese bajo disco-pop es imposible de sacar de la cabeza. Energía confiada y fresca.",
            "enlace_youtube": "https://www.youtube.com/watch?v=eVli-tstM5E"
        },
        {
            "id_mix": 2,
            "usuario_curador": "@Pop_Perfection",
            "titulo_mix": "Pop & Synth-Glow",
            "nombre_cancion": "Please Please Please - Sabrina Carpenter",
            "descripcion_cancion": "Mezcla brillante de Pop retro con letras irónicas y súper honestas.",
            "enlace_youtube": "https://www.youtube.com/watch?v=QFcv5Ma8u8k"
        },
        {
            "id_mix": 3,
            "usuario_curador": "@Pop_Perfection",
            "titulo_mix": "Pop & Synth-Glow",
            "nombre_cancion": "Cruel Summer - Taylor Swift",
            "descripcion_cancion": "El puente de esta canción es catarsis pura. Producción Synth-Pop adictiva.",
            "enlace_youtube": "https://www.youtube.com/watch?v=ic8j13piL3I"
        },
        # @Paulo_Mix
        {
            "id_mix": 4,
            "usuario_curador": "@Paulo_Mix",
            "titulo_mix": "Rock & Alternativo",
            "nombre_cancion": "Take Me Out - Franz Ferdinand",
            "descripcion_cancion": "El cambio de ritmo a la mitad te dispara la energía cuando llevas horas en la compu.",
            "enlace_youtube": "https://www.youtube.com/watch?v=X9jhwR07yk4"
        },
        {
            "id_mix": 5,
            "usuario_curador": "@Paulo_Mix",
            "titulo_mix": "Rock & Alternativo",
            "nombre_cancion": "Reptilia - The Strokes",
            "descripcion_cancion": "Guitarras gemelas rápidas y una batería impecable que no te deja perder el impulso.",
            "enlace_youtube": "https://www.youtube.com/watch?v=SlrxOm3rUCE"
        },
        {
            "id_mix": 6,
            "usuario_curador": "@Paulo_Mix",
            "titulo_mix": "Rock & Alternativo",
            "nombre_cancion": "The Pretender - Foo Fighters",
            "descripcion_cancion": "El intro empieza suave y explota poco a poco. Ideal para entrar en 'flow' total.",
            "enlace_youtube": "https://www.youtube.com/watch?v=SBjQ9tuuTJQ"
        },
        {
            "id_mix": 7,
            "usuario_curador": "@Paulo_Mix",
            "titulo_mix": "Rock & Alternativo",
            "nombre_cancion": "Everlong - Foo Fighters",
            "descripcion_cancion": "Energía constante de guitarras que te mantiene enfocado y motivado.",
            "enlace_youtube": "https://www.youtube.com/watch?v=AxuTd9rwEHQ"
        },
        # @Anna_LoFi
        {
            "id_mix": 8,
            "usuario_curador": "@Anna_LoFi",
            "titulo_mix": "Estudio & Relax",
            "nombre_cancion": "Feather - Nujabes",
            "descripcion_cancion": "Melodía clásica de piano para concentración profunda.",
            "enlace_youtube": "https://www.youtube.com/watch?v=P5-2-jD-4V4"
        },
        # @Gym_Beast
        {
            "id_mix": 9,
            "usuario_curador": "@Gym_Beast",
            "titulo_mix": "Energía & Gym",
            "nombre_cancion": "Murder In My Mind - Kordhell",
            "descripcion_cancion": "Phonk pesado para mantener la intensidad arriba en el entrenamiento.",
            "enlace_youtube": "https://www.youtube.com/watch?v=w-sQRS-Up9g"
        },
        # @Retro_Vibes
        {
            "id_mix": 10,
            "usuario_curador": "@Retro_Vibes",
            "titulo_mix": "Nocturno & Driving",
            "nombre_cancion": "Midnight City - M83",
            "descripcion_cancion": "Ese saxofón al final mientras ves las luces de la ciudad de noche.",
            "enlace_youtube": "https://www.youtube.com/watch?v=KRp0hBLqhX8"
        }
    ])
    df_mixes.to_csv(MIXES_FILE, index=False)

def load_data():
    df_curadores = pd.read_csv(CURADORES_FILE)
    df_mixes = pd.read_csv(MIXES_FILE)
    return df_curadores, df_mixes

# ==========================================
# 3. CONTROL DE ESTADO (SESSION STATE)
# ==========================================
if "vista" not in st.session_state:
    st.session_state.vista = "inicio"

if "curador_seleccionado" not in st.session_state:
    st.session_state.curador_seleccionado = None

if "seccion_activa" not in st.session_state:
    st.session_state.seccion_activa = "Descubrir"

# ==========================================
# 4. VISTAS DE LA APLICACIÓN
# ==========================================

def render_header():
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown('<div class="brand-logo">Soni<span>Qra</span></div>', unsafe_allow_html=True)
    with col2:
        m1, m2, m3 = st.columns(3)
        with m1:
            if st.button("Descubrir", use_container_width=True):
                st.session_state.vista = "inicio"
                st.session_state.seccion_activa = "Descubrir"
                st.rerun()
        with m2:
            if st.button("Directorio", use_container_width=True):
                st.session_state.vista = "inicio"
                st.session_state.seccion_activa = "Directorio"
                st.rerun()
        with m3:
            if st.button("Mix del Día", use_container_width=True):
                st.session_state.curador_seleccionado = "@Paulo_Mix"
                st.session_state.vista = "perfil_curador"
                st.rerun()

def render_inicio(df_curadores, df_mixes):
    render_header()

    st.markdown("""
    <div class="hero-container">
        <div class="hero-subtitle">PERSONAS REALES · MÚSICA REAL</div>
        <div class="hero-title">¿Cansado de la IA fría? Descubre música que tiene alma</div>
        <p style="color: #94A3B8; font-size: 1.1rem; max-width: 600px; margin: 0 auto 30px auto;">
            Cero algoritmos robóticos. Si existe en tu vida, una persona real ya le armó un mix perfecto en YouTube.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_search, col_btn = st.columns([4, 1])
    with col_search:
        busqueda = st.text_input("🔍 Busca una vibra, género o curador:", placeholder="Busca una vibra: estudiar, cocinar, noche...", label_visibility="collapsed")
    with col_btn:
        st.button("+ Ser Curador", use_container_width=True, type="primary")

    st.markdown("---")
    
    if st.session_state.seccion_activa == "Directorio":
        st.markdown("### 📚 Directorio Completo de Curadores")
    else:
        st.markdown("### 🎧 Encuentra a tu persona musical")

    if busqueda:
        df_filtrado = df_curadores[
            df_curadores['nombre'].str.contains(busqueda, case=False, na=False) |
            df_curadores['usuario'].str.contains(busqueda, case=False, na=False) |
            df_curadores['genero'].str.contains(busqueda, case=False, na=False)
        ]
    else:
        df_filtrado = df_curadores

    if df_filtrado.empty:
        st.info("No se encontraron curadores que coincidan con la búsqueda. ¡Intenta con otra vibra!")
    else:
        cols = st.columns(2)
        for idx, row in df_filtrado.reset_index(drop=True).iterrows():
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="soniqra-card">
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                        <div style="display: flex; align-items: center; gap: 12px;">
                            <span style="font-size: 2rem; background: #121518; padding: 10px; border-radius: 12px; border: 1px solid #2A2E33;">{row['icono_url_o_emoji']}</span>
                            <div>
                                <h4 style="margin: 0; color: #FFFFFF; font-size: 1.2rem;">{row['nombre']}</h4>
                                <span style="color: #00E6C3; font-size: 0.9rem;">{row['usuario']}</span>
                            </div>
                        </div>
                        <span class="badge-mint">{row['seguidores']} seguidores</span>
                    </div>
                    <div style="margin-bottom: 12px;">
                        <span class="badge-accent">{row['genero']}</span>
                    </div>
                    <p style="color: #CBD5E1; font-size: 0.95rem; line-height: 1.5; margin-bottom: 16px;">
                        {row['descripcion']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Ver perfil →", key=f"btn_{row['id_curador']}", use_container_width=True):
                    st.session_state.curador_seleccionado = row['usuario']
                    st.session_state.vista = "perfil_curador"
                    st.rerun()

    st.markdown("""
    <div class="form-container">
        <div style="color: #00E6C3; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px; margin-bottom: 5px;">¿NO ESTÁ EN EL DIRECTORIO?</div>
        <h3 style="color: #FFFFFF; margin-top: 0;">Solicitud de Curaduría de Emergencia</h3>
        <p style="color: #94A3B8;">Si buscas algo rarísimo, lo armamos en menos de 24 horas. Cuéntanos qué necesitas escuchar. ¿Quieres ser curador? Usa este mismo formulario y cuéntanos tu especialidad.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("form_emergencia"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            nombre_sol = st.text_input("Tu nombre")
            correo_sol = st.text_input("Tu correo")
        with col_f2:
            vibra_sol = st.text_input("Vibra o especialidad musical", placeholder="Ej. Rock noventero para trabajar")
            icono_sol = st.selectbox("Emoji Representativo", ["🎵", "🎸", "🎧", "☕", "🏎️", "⚡"])
            
        comentarios_sol = st.text_area("Cuéntanos más")
        btn_enviar = st.form_submit_button("Enviar Solicitud ✨", use_container_width=True)

        if btn_enviar:
            if nombre_sol and correo_sol and vibra_sol:
                nuevo_id = int(df_curadores['id_curador'].max() + 1) if not df_curadores.empty else 1
                nuevo_curador = pd.DataFrame([{
                    "id_curador": nuevo_id,
                    "nombre": nombre_sol,
                    "usuario": f"@{nombre_sol.replace(' ', '').lower()}",
                    "genero": vibra_sol,
                    "seguidores": 1,
                    "icono_url_o_emoji": icono_sol,
                    "descripcion": comentarios_sol if comentarios_sol else "Curador emergente explorando nuevas vibras."
                }])
                
                df_actualizado = pd.concat([df_curadores, nuevo_curador], ignore_index=True)
                df_actualizado.to_csv(CURADORES_FILE, index=False)
                st.success("¡Solicitud enviada con éxito! Se ha registrado en la base de datos de curadores.")
                st.rerun()
            else:
                st.warning("Por favor completa al menos tu nombre, correo y la vibra deseada.")

def render_perfil(df_curadores, df_mixes):
    if st.button("⬅ Volver al inicio", key="back_btn"):
        st.session_state.vista = "inicio"
        st.rerun()

    usuario_curador = st.session_state.curador_seleccionado
    curador = df_curadores[df_curadores['usuario'] == usuario_curador]

    if curador.empty:
        st.error("Curador no encontrado.")
        return

    curador = curador.iloc[0]

    st.markdown(f"""
    <div class="soniqra-card" style="margin-top: 15px; border-color: #FF5722;">
        <div style="display: flex; align-items: center; gap: 20px;">
            <span style="font-size: 3.5rem; background: #121518; padding: 15px; border-radius: 20px; border: 1px solid #2A2E33;">{curador['icono_url_o_emoji']}</span>
            <div>
                <div style="color: #00E6C3; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase;">CURADOR / {curador['genero']}</div>
                <h2 style="margin: 0; color: #FFFFFF; font-size: 2.2rem;">{curador['nombre']}</h2>
                <div style="margin: 6px 0;">
                    <span style="color: #00E6C3; font-weight: 700; font-size: 1.1rem; margin-right: 15px;">{curador['usuario']}</span>
                    <span class="badge-accent">{curador['seguidores']} seguidores</span>
                </div>
                <p style="color: #CBD5E1; margin-top: 10px; font-size: 1rem;">{curador['descripcion']}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    mixes_curador = df_mixes[df_mixes['usuario_curador'] == usuario_curador]

    if mixes_curador.empty:
        st.info("Este curador aún no ha publicado un mix específico.")
    else:
        titulo_mix = mixes_curador['titulo_mix'].iloc[0]
        
        st.markdown(f"""
        <div style="margin-top: 30px; margin-bottom: 20px;">
            <div style="color: #00E6C3; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px;">MIX PRINCIPAL · YOUTUBE</div>
            <h3 style="color: #FFFFFF; margin: 4px 0 0 0;">{titulo_mix}</h3>
            <p style="color: #94A3B8; font-size: 0.95rem;">Selección humana, canción por canción.</p>
        </div>
        """, unsafe_allow_html=True)

        for idx, song in mixes_curador.iterrows():
            st.markdown(f"""
            <div class="soniqra-card" style="padding: 18px; margin-bottom: 12px; background-color: #121518;">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                    <div>
                        <h4 style="margin: 0 0 6px 0; color: #FFFFFF; font-size: 1.1rem;">🎵 {song['nombre_cancion']}</h4>
                        <p style="color: #94A3B8; font-size: 0.95rem; margin: 0;">{song['descripcion_cancion']}</p>
                    </div>
                    <div>
                        <a href="{song['enlace_youtube']}" target="_blank" style="text-decoration: none;">
                            <button style="background-color: #00E6C3; color: #121518; border: none; padding: 10px 20px; border-radius: 10px; cursor: pointer; font-weight: 700; font-size: 0.95rem; display: flex; align-items: center; gap: 8px;">
                                ▶ Escuchar en YouTube ↗
                            </button>
                        </a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def main():
    inject_custom_css()
    init_data()
    df_curadores, df_mixes = load_data()

    if st.session_state.vista == "inicio":
        render_inicio(df_curadores, df_mixes)
    elif st.session_state.vista == "perfil_curador":
        render_perfil(df_curadores, df_mixes)

if __name__ == "__main__":
    main()