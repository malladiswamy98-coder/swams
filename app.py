import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="SYSTEM BREACH...", page_icon="💀", layout="centered")

# Hacker Style HTML & CSS
hacker_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { 
            background-color: black; 
            color: #0f0; 
            font-family: 'Courier New', monospace; 
            margin: 0; 
            overflow: hidden; 
            height: 100vh; 
            display: flex; 
            flex-direction: column; 
            justify-content: center; 
            align-items: center; 
        }
        #hacking-ui { 
            width: 95%; 
            height: 80%; 
            border: 2px solid #0f0; 
            background: rgba(0, 20, 0, 0.9); 
            padding: 20px; 
            box-shadow: 0 0 30px #0f0; 
            animation: shake 0.1s infinite; 
        }
        @keyframes shake { 
            0% { transform: translate(1px, 1px); } 
            50% { transform: translate(-2px, -1px); } 
            100% { transform: translate(1px, -1px); } 
        }
        .line { margin-bottom: 8px; font-size: 16px; color: #0f0; font-weight: bold; }
        #final-msg { 
            display: none; 
            text-align: center; 
            color: white; 
            text-shadow: 0 0 20px #0f0; 
        }
        .skull-text { 
            font-size: 30px; 
            color: red; 
            margin-bottom: 10px; 
            animation: blink 0.5s infinite; 
            font-weight: bold; 
        }
        @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }
    </style>
</head>
<body>
    <div id="hacking-ui">
        <div id="terminal"></div>
    </div>
    
    <div id="final-msg">
        <div class="skull-text">💀 SYSTEM DESTROYED BY SWAMY 💀</div>
        <p style="font-size: 20px;">"Rey! Bayapadaku Maya... Just Surprise anthe! 😂"</p>
        <p style="color: #0f0; font-size: 16px;">Mastermind: <b>MALLADI SWAMY</b></p>
    </div>

    <script>
        const terminal = document.getElementById('terminal');
        const commands = [
            "> INITIALIZING KERNEL EXPLOIT...",
            "> BYPASSING FIREWALL... [SUCCESS]",
            "> IP ADDRESS LOCATED: 192.168.1.39",
            "> ACCESSING PRIVATE GALLERY...",
            "> DOWNLOADING CONTACTS...",
            "> SYSTEM VULNERABILITY: 100% EXPOSED",
            "> INJECTING MALLADI-SWAMY-VIRUS.EXE...",
            "> DELETING SYSTEM LOGS...",
            "> REMOTE CONTROL GRANTED TO SWAMY",
            "> CRITICAL ERROR: CPU OVERHEATING!!!",
            "> HACKING COMPLETE. SHUTTING DOWN..."
        ];

        let i = 0;
        const timer = setInterval(() => {
            if (i < commands.length) {
                const line = document.createElement('div');
                line.className = 'line';
                line.innerHTML = commands[i];
                terminal.appendChild(line);
                i++;
            } else {
                clearInterval(timer);
                setTimeout(() => {
                    document.getElementById('hacking-ui').style.display = 'none';
                    document.getElementById('final-msg').style.display = 'block';
                }, 2500);
            }
        }, 600);
    </script>
</body>
</html>
"""

# HTML ni Streamlit window lo render chesthundhi
st.components.v1.html(hacker_html, height=800)
