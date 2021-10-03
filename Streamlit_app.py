import streamlit as st
import pandas as pd

st.title('Clean up drone (CUD)')

st.sidebar.title('An automated GPS based water drone :')
st.sidebar.subheader('Parameters')



app_mode = st.sidebar.selectbox('Choose the App mode',
                                ['About App', 'Trash Detection', 'Trash Maps & Satistics' ,'Ressources']
                                )

if app_mode == 'About App':

    st.header('We are Milkyway team 🌌 :')

    st.write("Tons of our trash flows into our ocean, waterways, and Great Lakes every year. It is a complex and ever growing problem, and it’s up to everyone to play a role in the solution. In many places, plastic is the main type of debris that you will see as you walk along a beach. In other locations, construction debris or fishing gear may be a common sight.Single-use and disposable items are deeply ingrained in our everyday lives. If you look around right now, you will see many objects that you are eventually going to throw away. As a society, we have moved increasingly towards on-the-go lifestyles where we value the convenience of these disposable items.If we want to stop the flow of trash into our ocean and Great Lakes, everyone, including government, businesses, and people like you, will have to make some meaningful changes.The story of plastic is the story of all of us.That's why we ,Milkyway Team ,we chose this challenge because we are facing an ongoing environmental disaster in our world, and our oceans receive about 12 million tons of waste each year, presenting many ecosystem problems.Thinking about an idea of creating an Autonomus GPS Based Water Drone named CUD:CleanUp Drone Which detects ,Classifies ,Quantifies the debris and save the coordinates of the grabage patches .Then the collection phase comes from another ship ,weather a marine debris collecting ship  'THe mothership' where se are going to collect the garbage  or any one of the existing  ship that saved their ids as participants of this work!")
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            width: 350px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-chisld {
            width: 350px;
            margin-left: -350px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.image(
        'http://assets.stickpng.com/images/58429400a6515b1e0ad75acc.png')

elif app_mode=='Trash Detection':
    st.header('Live image from CUD Followed with our Trained trash detection Model :')
    st.image('244004523_299572778228007_7759875201321181312_n.png')
    st.header('Global Trash Location :')
    st.image('243890613_1492334621123932_2887498729844834288_n.png')
elif app_mode=='Trash Maps & Satistics':
    st.subheader('Raw data :')
    df = pd.read_csv("INFOS.csv")
    st.write(df)

    #Bar Chart
    st.write('Bar Chart :')
    st.bar_chart(df['Plastic trash'])
else :
    st.write("Resources page After  seeing Nasa ressoucres given to us like :  \n **Ocean's circulation** :Due to the oceans current movement ,the plastic waste that flows end up in places where the flow of current is stagnant creating what we call garbage patches so that CUD can be in the right place and the right time and completes its mission efficiently . \n **GPS DATA** :to localize the most damaged areas around the world. \n **The US Federal Strategy for Addressing the Global Issue of Marine Litter** : It's a actually a pdf summerizing how the US is trying to solve the problems and which projects it has worked on .Reading it actually ,motivated us as a team and ispired us tremendously")

