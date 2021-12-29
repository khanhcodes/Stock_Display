mkdir -p ~/.streamlit/
echo "[theme]
primaryColor = '#9cb4ff'
backgroundColor = '#202020'
secondaryBackgroundColor = '#B9F1C0'
textColor = '#FFFFFF'
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml