import streamlit as st
import streamlit.components.v1 as components


def render_speech_and_text_input(q_key, label="Your Answer:", default_val="", disabled=False):
    """
    Renders Voice Microphone Speech Recognition component + Answer Text Area.
    Converts spoken speech sentence-by-sentence and accumulates text until user clicks Stop.
    """
    if disabled:
        st.text_area(
            label=f"{label} [LOCKED ✓]",
            value=default_val,
            height=120,
            disabled=True,
            key=f"disabled_text_{q_key}"
        )
        return default_val

    st.markdown("**Select Input Method:** 🎤 Voice Microphone (Speech to Text) or ⌨️ Keyboard Text")

    input_mode = st.radio(
        "Input Method:",
        options=["🎤 Voice Microphone (Speech to Text)", "⌨️ Keyboard Text Area"],
        horizontal=True,
        key=f"radio_input_mode_{q_key}"
    )

    if input_mode == "🎤 Voice Microphone (Speech to Text)":
        st.caption("Click **'Start Continuous Recording'**, speak your answer sentence-by-sentence. Speech recognition will continue recording until you click **'Stop'**.")

        speech_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 4px; background: transparent; }}
                .mic-container {{ background: #f8fafc; border: 1.5px solid #2563eb; border-radius: 12px; padding: 12px; box-shadow: 0 2px 8px rgba(37,99,235,0.08); }}
                .btn-group {{ display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 8px; align-items: center; }}
                .btn {{
                    background-color: #2563eb; color: white; border: none; padding: 8px 14px;
                    font-weight: bold; border-radius: 8px; cursor: pointer; font-size: 0.85rem;
                    display: inline-flex; align-items: center; gap: 4px; transition: all 0.2s;
                }}
                .btn:hover {{ background-color: #1d4ed8; }}
                .btn-stop {{ background-color: #dc2626; }}
                .btn-stop:hover {{ background-color: #b91c1c; }}
                .btn-copy {{ background-color: #059669; }}
                .btn-copy:hover {{ background-color: #047857; }}
                .btn-clear {{ background-color: #64748b; }}
                .btn-clear:hover {{ background-color: #475569; }}
                .recording-pulse {{
                    display: inline-block; width: 10px; height: 10px; background-color: #ef4444;
                    border-radius: 50%; margin-right: 6px; animation: pulse 1.2s infinite;
                }}
                @keyframes pulse {{
                    0% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }}
                    70% {{ transform: scale(1.1); box-shadow: 0 0 0 8px rgba(239, 68, 68, 0); }}
                    100% {{ transform: scale(0.95); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }}
                }}
                .status {{ font-size: 0.83rem; color: #334155; font-weight: 600; margin-bottom: 6px; min-height: 20px; }}
                .output-box {{
                    width: 98%; background: white; border: 1px solid #cbd5e1; border-radius: 8px;
                    padding: 8px 10px; font-size: 0.9rem; color: #0f172a; min-height: 55px; max-height: 110px;
                    overflow-y: auto; box-sizing: border-box; line-height: 1.4;
                }}
            </style>
        </head>
        <body>
            <div class="mic-container">
                <div class="btn-group">
                    <button class="btn" id="startBtn" onclick="startSpeech()">🎤 Start Continuous Recording</button>
                    <button class="btn btn-stop" id="stopBtn" onclick="stopSpeech()">⏹️ Stop</button>
                    <button class="btn btn-copy" id="copyBtn" onclick="copySpeech()">📋 Copy Spoken Text</button>
                    <button class="btn btn-clear" id="clearBtn" onclick="clearSpeech()">🗑️ Clear</button>
                </div>
                <div class="status" id="statusMsg">Status: Click 'Start Continuous Recording' and speak your response sentence by sentence.</div>
                <div class="output-box" id="speechResult">Your spoken sentences will accumulate here...</div>
            </div>

            <script>
                var recognition;
                var isListening = false;
                var finalTranscript = '';

                function startSpeech() {{
                    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {{
                        var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                        
                        if (!recognition) {{
                            recognition = new SpeechRecognition();
                        }}
                        
                        recognition.continuous = true;
                        recognition.interimResults = true;
                        recognition.lang = 'en-US';

                        isListening = true;

                        document.getElementById('statusMsg').innerHTML = '<span class="recording-pulse"></span> <strong>Status: Recording... Speak sentence after sentence continuously until you click STOP.</strong>';

                        recognition.onresult = function(event) {{
                            var interimTranscript = '';
                            for (var i = event.resultIndex; i < event.results.length; ++i) {{
                                if (event.results[i].isFinal) {{
                                    var text = event.results[i][0].transcript.trim();
                                    if (text) {{
                                        if (finalTranscript && !finalTranscript.endsWith(' ')) {{
                                            finalTranscript += ' ';
                                        }}
                                        finalTranscript += text;
                                        if (!text.endsWith('.') && !text.endsWith('?') && !text.endsWith('!')) {{
                                            finalTranscript += '.';
                                        }}
                                    }}
                                }} else {{
                                    interimTranscript += event.results[i][0].transcript;
                                }}
                            }}
                            var fullText = finalTranscript + (interimTranscript ? ' ' + interimTranscript : '');
                            document.getElementById('speechResult').innerText = fullText || "Listening for speech...";
                        }};

                        recognition.onerror = function(event) {{
                            if (event.error === 'no-speech') {{
                                return;
                            }}
                            console.log('Speech error:', event.error);
                            if (event.error === 'not-allowed' || event.error === 'service-not-allowed') {{
                                isListening = false;
                                document.getElementById('statusMsg').innerText = "Status: Microphone permission denied. Please allow microphone access or use keyboard input.";
                            }}
                        }};

                        recognition.onend = function() {{
                            if (isListening) {{
                                try {{
                                    recognition.start();
                                }} catch(e) {{
                                    console.log('Restart exception:', e);
                                }}
                            }} else {{
                                document.getElementById('statusMsg').innerText = "Status: Recording stopped ✓. Click 'Copy Spoken Text' and paste into the answer box below.";
                            }}
                        }};

                        try {{
                            recognition.start();
                        }} catch(e) {{
                            console.log('Start exception:', e);
                        }}
                    }} else {{
                        document.getElementById('statusMsg').innerText = "Web Speech API is not supported in this browser. Please use Chrome or Edge, or type in the text box below.";
                    }}
                }}

                function stopSpeech() {{
                    isListening = false;
                    if (recognition) {{
                        try {{
                            recognition.stop();
                        }} catch(e) {{}}
                    }}
                    document.getElementById('statusMsg').innerText = "Status: Stopped ✓. Transcribed sentences saved above. Click 'Copy Spoken Text' or copy directly into answer box.";
                }}

                function copySpeech() {{
                    var text = document.getElementById('speechResult').innerText;
                    if (text && text !== "Your spoken sentences will accumulate here..." && text !== "Listening for speech...") {{
                        navigator.clipboard.writeText(text).then(function() {{
                            document.getElementById('statusMsg').innerText = "Copied to clipboard! ✅ Paste (Ctrl+V) into the answer box below for evaluation.";
                        }}).catch(function(err) {{
                            var range = document.createRange();
                            range.selectNode(document.getElementById('speechResult'));
                            window.getSelection().removeAllRanges();
                            window.getSelection().addRange(range);
                            document.getElementById('statusMsg').innerText = "Text selected! Press Ctrl+C to copy, then paste into the answer box below.";
                        }});
                    }} else {{
                        document.getElementById('statusMsg').innerText = "No spoken text to copy yet. Click Start and speak your response.";
                    }}
                }}

                function clearSpeech() {{
                    finalTranscript = '';
                    document.getElementById('speechResult').innerText = "Your spoken sentences will accumulate here...";
                    document.getElementById('statusMsg').innerText = "Cleared. Click 'Start Continuous Recording' to begin new recording.";
                }}
            </script>
        </body>
        </html>
        """
        components.html(speech_html, height=195)

    # Streamlit text area (Editable answer box used for evaluation)
    text_key = f"ans_text_box_{q_key}"
    if text_key not in st.session_state:
        st.session_state[text_key] = default_val

    user_text = st.text_area(
        label=label,
        value=st.session_state[text_key],
        height=120,
        key=text_key,
        placeholder="Type or paste your spoken response here..."
    )

    return user_text
