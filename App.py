import streamlit as st
from openai import OpenAI  
from pydantic import BaseModel, Field



class HookVariation(BaseModel):
    optimized_hook: str = Field(description="The newly generated, highly engaging hook.")
    psychological_trigger: str = Field(description="The psychological reason why this new hook works better.")
    score: int = Field(description="An engagement score from 1 to 100 for the new hook.")

class OptimizedHooksResponse(BaseModel):
    original_hook: str = Field(description="The original weak hook provided by the user.")
    hooks: list[HookVariation] = Field(description="A list of exactly 5 distinct optimized hook variations.")




import os
OPENAI_STRICT_METRIC_KEY = "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" # 👈 PASTE YOUR ACTUAL GROQ API KEY HERE inside the quotes

client = OpenAI(
    base_url="https://api.groq.com/openai/v1", 
    api_key=OPENAI_STRICT_METRIC_KEY
)


st.set_page_config(
    page_title="FIRST 3SEC AI | Creator Dashboard", 
    page_icon="⚡", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)


with st.sidebar:
    st.title("⚡ FIRST 3SEC AI")
    st.markdown("---")
    st.header("Settings")

    model_choice = st.selectbox(
        "Choose Model",
        ["llama-3.3-70b-versatile"]
    )

    st.markdown("---")
    st.info("Paste your hook and optimize it.")


st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #0a0b0d;
    }
    
    /* PPT Exact Branding Identity Header - FORCED MASSIVE SCALE */
    .brand-title {
        background: linear-gradient(135deg, #ccff00 0%, #a855f7 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 800 !important;
        font-size: 5.5rem !important; /* Forced massive display size */
        letter-spacing: -0.04em !important;
        margin-bottom: 0px !important;
        line-height: 1.0;
        display: block;
    }
    .brand-tagline {
        color: #f3f4f6;
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 15px;
        margin-bottom: 2px;
    }
    .brand-subtext {
        color: #6b7280;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 2rem;
    }
    
    /* Pitch-Deck Hook Failure Pain Callout Box */
    .pain-callout {
        background: rgba(239, 68, 68, 0.06);
        border: 1px dashed rgba(239, 68, 68, 0.3);
        border-radius: 12px;
        padding: 15px;
        color: #fca5a5;
        font-size: 0.95rem;
        margin-bottom: 20px;
    }
    
    /* Premium Architecture Output Display Matrix */
    .matrix-card {
        background: rgba(22, 24, 33, 0.8);
        border: 1px solid rgba(204, 255, 0, 0.2);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        transition: all 0.3s ease-in-out;
    }
    .matrix-card:hover {
        border-color: rgba(204, 255, 0, 0.7);
        box-shadow: 0 10px 30px -10px rgba(204, 255, 0, 0.15);
        transform: translateY(-2px);
    }
    
    .hook-text {
        color: #ffffff;
        font-size: 1.25rem;
        font-weight: 600;
        line-height: 1.5;
        border-left: 4px solid #ccff00;
        padding-left: 14px;
        margin-bottom: 15px;
    }
    
    .badge {
        background: rgba(204, 255, 0, 0.12);
        color: #ccff00;
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('<span class="brand-title" style="background: linear-gradient(135deg, #ccff00 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 5.5rem; font-weight: 800;">FIRST 3SEC AI.</span>', unsafe_allow_html=True)
st.markdown('<p class="brand-tagline">The Only Window That Matters. ⚡</p>', unsafe_allow_html=True)
st.markdown('<p class="brand-subtext">Powered by gpt-4o-mini & Pydantic Validation Matrix</p>', unsafe_allow_html=True)


col_input, col_pitch = st.columns([5, 3], gap="large")

with col_input:
    st.markdown("### 🖋️ Paste Raw Script Idea or Topic")
    weak_hook_input = st.text_area(
        "Input Draft",
        placeholder="e.g., How to post like a pro / 3 tips for video editing...",
        height=140,
        label_visibility="collapsed"
    )
    
    
    run_pipeline = st.button("Re-Engineer First 3 Seconds", type="primary", use_container_width=True)

with col_pitch:
    st.markdown("### 🎭 Retention Pain-Point")
    st.markdown(
        '<div class="pain-callout"><strong>"Creators don’t lose the video. They lose the first three seconds."</strong><br>'
        'Stop wasting hours manual-scripting variations and guessing audience retention frameworks.</div>', 
        unsafe_allow_html=True
    )
    
    with st.expander("🗿 Who bleeds when a hook fails?", expanded=False):
        st.markdown("""
        * **Creators:** Discouraged by hours of editing trapped in single-digit views.
        * **Editors:** High-quality cuts go completely unseen because of a slow intro.
        * **Brands:** Sponsorship budgets burn out on dead retention drop-offs.
        """)

st.markdown("---")


if run_pipeline:
    if not weak_hook_input.strip():
        st.warning("Please enter your draft idea or transcript first!")
    else:
        status_text = st.empty()
        
        with st.spinner("Processing through retention pipeline..."):
            status_text.info("🔄 Stage 03: Injecting strict Pydantic structural archetypes...")
            
            
            try:
                status_text.info("🔃 Stage 04: Mining OpenAI Chat Completions Proxy Matrix...")
                
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile", 
                    response_format={"type": "json_object"},
                    messages=[
                        {
                            "role": "system", 
                            "content": (
                                "You are an expert copywriter. Your job is to take a weak hook and generate exactly 5 diverse optimized variations. "
                                "CRITICAL SCORING RULE: The 'score' field must represent an engagement percentage out of 100. "
                                "Since these are highly optimized viral hooks, you MUST score them between 85 and 98 based on their psychological impact. "
                                "NEVER give single-digit scores like 5, 7, or 8.\n\n"
                                "You MUST return a JSON object that adheres perfectly to this structure:\n"
                                '{"original_hook": "string", "hooks": [{"optimized_hook": "string", "psychological_trigger": "string", "score": integer}]}'
                            )
                        },
                        {
                            "role": "user", 
                            "content": f"Optimize this weak hook: {weak_hook_input}"
                        }
                    ]
                )
                
                
                status_text.info("🕵️ Stage 05: Verifying structured JSON output arrays against schema matrix...")
                import json
                raw_json = response.choices[0].message.content
                
                structured_data = OptimizedHooksResponse.parse_raw(raw_json)
                
                
                status_text.empty()
                st.toast("Structural variants compiled completely!", icon="⚡")
                
                st.markdown("## 🌞 Optimized Shelves Matrix")
                st.markdown(f"Original Draft Baseline: *\"{structured_data.original_hook}\"*")
                st.write("")
                
                for idx, hook_item in enumerate(structured_data.hooks, 1):
                    
                    st.markdown(f"""
                        <div class="matrix-card">
                            <span class="badge">Psychological Archetype 0{idx}</span>
                            <div style="margin-top: 12px;" class="hook-text">"{hook_item.optimized_hook}"</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    col_metric, col_trigger = st.columns([1, 3])
                    with col_metric:
                        st.metric(
                            label="📈Virality Score Index", 
                            value=f"{hook_item.score}%",
                            help="Retention predictability rate determined by historical framework criteria."
                        )
                        st.progress(hook_item.score)
                    with col_trigger:
                        st.markdown(f"**Historical Retention Framework Strategy:**")
                        st.caption(f"_{hook_item.psychological_trigger}_")
                    
                    st.markdown('<div style="margin-bottom: 25px;"></div>', unsafe_allow_html=True)
                                            
            except Exception as e:
                status_text.empty()
                st.error(f"An error occurred in the pipeline engine: {e}")
