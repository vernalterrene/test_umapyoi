import streamlit as st


umas = {
    "Agnes Tachyon": ["A", "G", "G", "D", "A", "B", "E", "A", "B", "F", "U=ma2"],
    "Mejiro Ryan": ["A", "G", "E", "C", "A", "B", "F", "A", "A", "F", "Let's Pump Some Iron"],
    "Winning Ticket": ["A", "G", "G", "F", "A", "B", "G", "F", "A", "G", "Our Ticket to Win!"],
    "Sakura Bakushin O": ["A", "G", "A", "B", "G", "G", "A", "A", "F", "G", "Genius x Bakushin = Victory"],
    "Haru Urara": ["G", "A", "A", "B", "G", "G", "G", "G", "A", "B", "Super-duper Climax"],
    "Matikane Fukukitaru": ["A", "F", "F", "C", "A", "A", "G", "B", "A", "F", "I See Victory in My Future"],
    "Nice Nature": ["A", "G", "G", "C", "A", "A", "F", "B", "A", "D", "Just a Little Farther"],
    "King Halo": ["A", "G", "A", "B", "B", "C", "G", "B", "A", "D", "Prideful King"]
}

races = [
    "Arima Kinen","Asahi Hai Futurity Stakes","Champions Cup","February Stakes","Hanshin Juvenile Fillies","Hopeful Stakes","Japan Cup","Japan Dirt Derby","JBC Classic","JBC Ladies' Classic","JBC Sprint","Japanese Oaks","Kikuka Sho","Mile Championship","NHK Mile Cup","Oka Sho","Osaka Hai","Queen Elizabeth II Cup","Satsuki Sho","Shuka Sho","Sprinters Stakes","Takamatsunomiya Kinen","Takarazuka Kinen","Teio Sho","Tenno Sho (Autumn)","Tenno Sho (Spring)","Tokyo Daishoten","Tokyo Yushun (Japanese Derby)","URA Finale","Victoria Mile","Yasuda Kinen"
]

gradeBound = {
    "SS+": 1200,
    "SS": 1100,
    "S+": 1050,
    "S": 1000,
    "A+": 900,
    "A": 900,
    "B+": 700,
    "B": 600,
    "C+": 500,
    "C": 400,
    "D+": 350,
    "D": 300,
    "E+": 250,
    "E": 200,
    "F+": 150,
    "F": 100,
    "G+": 50,
    "G": 0
}

def return_letter_grade(score):
    for letter in gradeBound.keys():
        if score >= gradeBound[letter]:
            return letter



# ---- LAYOUT ----
st.set_page_config(
    page_title="Uma Logger",
    page_icon="🐴",
)

st.title("🐴🌟 My Best Umas")
st.text("Just take a screenshot of ur horse tbh HAGHAHA oh well i just wanted to try the forms n passing stuff between pages...")
st.divider()



# ---- CARD LAYOUT ----
if "finishedUma" in st.session_state and st.session_state.finishedUma:
    for finishedStats in st.session_state.finishedUma:
        outputCard = st.expander(finishedStats["titleCard"])
        with outputCard:
            st.header("Stats") 
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.write(f"Speed: **{return_letter_grade(finishedStats['stats'][0])}**  *{finishedStats['stats'][0]}*")
            with col2:
                st.write(f"Stamina: **{return_letter_grade(finishedStats['stats'][1])}**  *{finishedStats['stats'][1]}*")
            with col3:
                st.write(f"Power: **{return_letter_grade(finishedStats['stats'][2])}**  *{finishedStats['stats'][2]}*")
            with col4:
                st.write(f"Guts: **{return_letter_grade(finishedStats['stats'][3])}**  *{finishedStats['stats'][3]}*")
            with col5:
                st.write(f"Wit: **{return_letter_grade(finishedStats['stats'][4])}**  *{finishedStats['stats'][4]}*")

            st.subheader("Track") 
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(f"Turf: **{finishedStats['track'][0]}**")
            with col2:
                st.write(f"Dirt: **{finishedStats['track'][1]}**")

            st.subheader("Distance") 
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(f"Sprint: **{finishedStats['distance'][0]}**")
            with col2:
                st.write(f"Mile: **{finishedStats['distance'][1]}**")
            with col3:
                st.write(f"Medium: **{finishedStats['distance'][2]}**")
            with col4:
                st.write(f"Long: **{finishedStats['distance'][3]}**")
                
            st.subheader("Style") 
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(f"Front: **{finishedStats['style'][0]}**")
            with col2:
                st.write(f"Pace: **{finishedStats['style'][1]}**")
            with col3:
                st.write(f"Late: **{finishedStats['style'][2]}**")
            with col4:
                st.write(f"End: **{finishedStats['style'][3]}**")
            st.divider()

            st.header("Sparks")
            col1, col2, col3 = st.columns(3)
            with col1:
                blueString = f"{finishedStats['blueSparkValue'][1]}★ {finishedStats['blueSparkValue'][0]}"
                st.info(blueString)
            with col2:
                pinkString = f"{finishedStats['pinkSparkValue'][1]}★ {finishedStats['pinkSparkValue'][0]}"
                st.error(pinkString)
            with col3:
                if 'uniqSparkValue' in finishedStats:
                    greenString = f"{finishedStats['uniqSparkValue'][1]}★ {finishedStats['uniqSparkValue'][0]}"
                    st.success(greenString)
                else:
                    st.write("")
            
            if 'whiteSparks' in finishedStats:
                numWhiteSparks = len(finishedStats["whiteSparks"])
                numRows = (numWhiteSparks//3)+1 
                finalWhiteSparkList = finishedStats["whiteSparks"]
                if "whiteSparks" in finishedStats and finishedStats["whiteSparks"]:
                    cols = st.columns(4)
                    for i, spark in enumerate(finishedStats["whiteSparks"]):
                        with cols[i % 4]:
                            st.badge(spark, color="grey")
            st.write("")
else:
    st.warning("No Umas have been added yet. Go to the 'Add Uma' page to add horse girls.")

if st.button("Clear All"):
  if "finishedUma" in st.session_state:
    for key in st.session_state.keys():
        del st.session_state[key]
st.write("")