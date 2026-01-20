import streamlit as st
import random

st.set_page_config(page_title="Unhinged Email Closings", page_icon="📧")

st.title("📧 Unhinged Email Closings Generator")
st.write(
    "Generate email closings that range from *corporately detached* "
    "to *emotionally unwell*."
)

# --- Controls ---
level = st.slider(
    "Unhinged level",
    min_value=1,
    max_value=5,
    value=3
)

tone = st.slider(
    "Tone",
    min_value=0,
    max_value=100,
    value=50,
    help="0 = Corporate | 100 = Feral"
)

style = st.selectbox(
    "Style intent",
    [
        "Neutral",
        "Passive-aggressive",
        "Existential",
        "Chaotic",
        "Burnt out",
    ]
)

# --- Data ---
sentences = {
    "Neutral": {
        1: ["Please let me know if you have any questions."],
        2: ["Feel free to reach out if needed."],
        3: ["No follow-up is required unless absolutely necessary."],
        4: ["I will assume no response means this is resolved."],
        5: ["Silence will be taken as mutual understanding."]
    },
    "Passive-aggressive": {
        1: ["Let me know if anything is unclear."],
        2: ["I trust this explains everything."],
        3: ["This should be self-explanatory."],
        4: ["I believe this answers any remaining questions."],
        5: ["Further clarification feels unlikely to be productive."]
    },
    "Existential": {
        1: ["Looking forward to your thoughts."],
        2: ["I await your response in due time."],
        3: ["I will wait and see what happens."],
        4: ["Time will tell if a response arrives."],
        5: ["Whether or not this is acknowledged is out of my control."]
    },
    "Chaotic": {
        1: ["Let me know your thoughts."],
        2: ["Respond whenever."],
        3: ["No pressure to reply."],
        4: ["Reply if the universe aligns."],
        5: ["Do not reply unless compelled by fate."]
    },
    "Burnt out": {
        1: ["Thanks in advance."],
        2: ["Thanks."],
        3: ["Thank you, I guess."],
        4: ["Thanks for reading this far."],
        5: ["Thank you for existing in this email thread."]
    },
}

sign_offs = {
    "corporate": [
        "Kind regards,",
        "Best regards,",
        "Sincerely,",
    ],
    "neutral": [
        "Best,",
        "Thanks,",
        "Regards,",
    ],
    "feral": [
        "No follow-ups asked,",
        "With minimal expectations,",
        "In quiet resignation,",
        "Warm-ish regards,",
    ]
}

# --- Logic ---
sentence = random.choice(sentences[style][level])

if tone < 33:
    signoff = random.choice(sign_offs["corporate"])
elif tone < 66:
    signoff = random.choice(sign_offs["neutral"])
else:
    signoff = random.choice(sign_offs["feral"])

full_closing = f"{sentence}\n\n{signoff}\n[Your Name]"

# --- Output ---
if st.button("Generate email closing"):
    st.markdown("### ✉️ Your email closing")
    st.code(full_closing, language="text")

    st.download_button(
        label="📋 Copy to clipboard",
        data=full_closing,
        file_name="email_closing.txt",
        mime="text/plain"
    )

st.markdown("---")
st.caption("Use responsibly. Or irresponsibly. We’re not your manager.")
