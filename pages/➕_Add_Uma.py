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



# ---- SESSION TRACKER THING ----
if "finishedUma" not in st.session_state:
    st.session_state.finishedUma = []
if "form_id" not in st.session_state: #give each form a unique id
    st.session_state.form_id = 0 
sessNumTracker = len(st.session_state.finishedUma)



# ---- FORM LAYOUT ----
st.set_page_config(
    page_title="Add Uma",
    page_icon="➕",
)

st.title("🐴➕ Add a Veteran Uma")
st.text("Pls click 'Switch Uma' to update placeholder stats and unique skill name...")
st.text("")

with st.form("add_form"):
    name_selection = st.selectbox("Select an Uma", umas.keys())
    note = st.text_input("Add a note for this horse.")
    st.form_submit_button('Switch Uma')
    st.divider()

    st.header("Stats") 
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        speed = st.number_input('Speed:', min_value=0, max_value=1200)
    with col2:
        stam = st.number_input('Stamina:', min_value=0, max_value=1200)
    with col3:
        pow = st.number_input('Power:', min_value=0, max_value=1200)
    with col4:
        guts = st.number_input('Guts:', min_value=0, max_value=1200)
    with col5:
        wit = st.number_input('Wit:', min_value=0, max_value=1200)

    st.subheader("Track") 
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        turf = st.text_input('Turf:', value=umas[name_selection][0], max_chars=1)
    with col2:
        dirt = st.text_input('Dirt:', value=umas[name_selection][1], max_chars=1)

    st.subheader("Distance") 
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        sprint = st.text_input('Sprint:', value=umas[name_selection][2], max_chars=1)
    with col2:
        mile = st.text_input('Mile:', value=umas[name_selection][3], max_chars=1)
    with col3:
        medium = st.text_input('Medium:', value=umas[name_selection][4], max_chars=1)
    with col4:
        long = st.text_input('Long:', value=umas[name_selection][5], max_chars=1)
        

    st.subheader("Style") 
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        front = st.text_input('Front:', value=umas[name_selection][6], max_chars=1)
    with col2:
        pace = st.text_input('Pace:', value=umas[name_selection][7], max_chars=1)
    with col3:
        late = st.text_input('Late:', value=umas[name_selection][8], max_chars=1)
    with col4:
        end = st.text_input('End:', value=umas[name_selection][9], max_chars=1) 
    st.divider()

    st.header("Sparks")
    col1, col2 = st.columns(2)
    with col1:
        blueSpark = st.selectbox("Blue Spark:", ['Speed', 'Stamina', 'Power', 'Guts', 'Wit'])
        blueSparkStars = st.radio("Number of Stars:", ['1','2','3'], key=f"blueStars_{st.session_state.form_id}")
    with col2:
        pinkSpark = st.selectbox("Pink Spark:", ['Turf', 'Dirt', 'Sprint', 'Mile', 'Medium', 'Long', 'Front Runner', 'Pace Chaser', 'Late Surger', 'End Closer'])
        pinkSparkStars = st.radio("Number of Stars:", ['1','2','3'], key=f"pinkStars_{st.session_state.form_id}")

    col1, col2 = st.columns(2)
    with col1:
        uniqSpark = st.selectbox("Green Spark:", ["None", umas[name_selection][10]])
        uniqSparkStars = st.radio("Number of Stars:", ['1','2','3'], key=f"uniqStars_{st.session_state.form_id}")

    st.subheader("White Sparks")
    raceSparkSelection = st.expander("Race Sparks")
    with raceSparkSelection:
        raceSpark = st.multiselect("Select races:", races)

    skillSparkSelection = st.expander("Skill Sparks")
    with skillSparkSelection:
        st.text("Not a complete list.")
        cornerSkillSelection = st.pills("XX Corner Skills:", [
            'Front Runner Corners', 'Pace Chaser Corners', 'Late Surger Corners', 'End Closer Corners',
            'Sprint Corners', 'Mile Corners', 'Medium Corners', 'Long Corners'], selection_mode="multi")
        straightSkillSelection = st.pills("XX Straightaways Skills:", [
            'Front Runner Straightaways', 'Pace Chaser Straightaways', 'Late Surger Straightaways', 'End Closer Straightaways',
            'Sprint Straightaways', 'Mile Straightaways', 'Medium Straightaways', 'Long Straightaways'], selection_mode="multi")
        staminaSkillSelection = st.pills("Stamina Skills:", [
            "After-school Stroll", "Calm in a Crowd", "Corner Recovery", "Deep Breaths", "Extra Tank", 
            "Hydrate", "Lay Low", "Moxie", "Pace Strategy", "Preferred Position", "Rosy Outlook", "Soft Step", 
            "Stamina to Spare", "Standing By", "Straightaway Recovery", "Watchful Eye"], selection_mode="multi")
    st.write("")

    finish = st.form_submit_button('Finish')



# ---- STORE NEW CARD INFO ----
if finish:    
    if not note:
        note = "Veteran Uma"

    finishedUma = {
        "titleCard": f"**{name_selection}:** {note}",
        "stats": [speed, stam, pow, guts, wit],
        "track": [turf, dirt],
        "distance": [sprint, mile, medium, long],
        "style": [front, pace, late, end],
        "blueSparkValue": [blueSpark, blueSparkStars],
        "pinkSparkValue": [pinkSpark, pinkSparkStars],
    }

    if uniqSpark != "None":
        finishedUma["uniqSparkValue"] = [uniqSpark, uniqSparkStars]

    whiteSparksList = []
    if raceSpark:
        whiteSparksList.extend(raceSpark)
    if cornerSkillSelection:
        whiteSparksList.extend(cornerSkillSelection)
    if straightSkillSelection:
        whiteSparksList.extend(straightSkillSelection)  
    if staminaSkillSelection:
        whiteSparksList.extend(staminaSkillSelection)   

    if whiteSparksList:
        finishedUma["whiteSparks"] = whiteSparksList  
    
    st.session_state.finishedUma.append(finishedUma)
    st.session_state.form_id += 1
    st.session_state.show_balloons = True
    st.rerun()
    
if "show_balloons" in st.session_state and st.session_state.show_balloons:
    st.balloons()
    del st.session_state.show_balloons
