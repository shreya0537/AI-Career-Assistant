import time
import streamlit as st
import streamlit.components.v1 as components


def get_or_start_round_timer(round_key, time_limit_seconds):
    """
    Initializes round_start_time ONCE when entering a round for the first time.
    Persists start_time across Streamlit reruns.
    """
    start_key = f"round_start_time_{round_key}"

    if start_key not in st.session_state or st.session_state[start_key] is None:
        st.session_state[start_key] = time.time()

    start_time = st.session_state[start_key]
    elapsed = time.time() - start_time
    remaining = max(0, int(time_limit_seconds - elapsed))

    mins, secs = divmod(remaining, 60)
    timer_str = f"{mins:02d}:{secs:02d}"

    is_expired = (remaining <= 0)
    return remaining, is_expired, timer_str


def render_round_timer_widget(round_name, round_key, time_limit_seconds, is_submitted=False):
    """
    Renders a live second-by-second countdown timer.
    Ticks every 1 second in the browser UI.
    Returns True if time has expired and round is not yet submitted.
    """
    if is_submitted:
        st.markdown(
            f"""
            <div style="background: #f0fdf4; border: 1.5px solid #22c55e; border-radius: 12px; padding: 10px 16px; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center;">
                <div style="font-weight: 700; color: #166534; font-size: 0.9rem;">
                    ⏱️ {round_name} Status
                </div>
                <div style="font-size: 1rem; font-weight: 800; color: #15803d;">
                    Round Submitted ✓ [LOCKED]
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        return False

    remaining, is_expired, timer_str = get_or_start_round_timer(round_key, time_limit_seconds)

    if is_expired:
        st.error(f"⏰ Time's up for {round_name}! Attempted answers are automatically being saved and locked...")
        return True

    # Live Second-by-Second Browser Countdown Timer Component
    timer_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; background: transparent; }}
            .timer-box {{
                background: #f8fafc;
                border: 1.5px solid #2563eb;
                border-radius: 12px;
                padding: 10px 18px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 2px 6px rgba(0,0,0,0.03);
            }}
            .timer-title {{ font-weight: 700; color: #1e293b; font-size: 0.9rem; }}
            .timer-clock {{ font-size: 1.2rem; font-weight: 800; color: #2563eb; letter-spacing: 0.05em; }}
            .timer-clock.warning {{ color: #ef4444; }}
        </style>
    </head>
    <body>
        <div class="timer-box" id="tBox">
            <div class="timer-title">⏱️ {round_name} Active Timer</div>
            <div class="timer-clock" id="tClock">Time Remaining: {timer_str}</div>
        </div>

        <script>
            var secondsLeft = {remaining};
            var clockEl = document.getElementById("tClock");
            var boxEl = document.getElementById("tBox");

            function updateClock() {{
                if (secondsLeft <= 0) {{
                    clockEl.innerText = "Time Remaining: 00:00 (Time's Up!)";
                    clockEl.className = "timer-clock warning";
                    boxEl.style.borderColor = "#ef4444";
                    return;
                }}

                var m = Math.floor(secondsLeft / 60);
                var s = secondsLeft % 60;
                var mStr = m < 10 ? "0" + m : "" + m;
                var sStr = s < 10 ? "0" + s : "" + s;

                clockEl.innerText = "Time Remaining: " + mStr + ":" + sStr;

                if (secondsLeft <= 60) {{
                    clockEl.className = "timer-clock warning";
                    boxEl.style.borderColor = "#ef4444";
                }}

                secondsLeft--;
            }}

            updateClock();
            setInterval(updateClock, 1000);
        </script>
    </body>
    </html>
    """
    components.html(timer_html, height=52)
    return False
