from crewai import Agent, Task, Crew, Process

from langchain_openai import ChatOpenAI
import os
import time

os.environ ["OPENAI_API_KEY"]="YOUR_API_KEY"
manager_llm=ChatOpenAI(model="gpt-4o")


researcher_politics = Agent (
    role='Researcher politics',
    goal='Research the ### political framework',
    backstory='You are an expert politic philosopher in the field of X',
    verbose=True,
    allow_delegation=False,
    cache=True,
)
researcher_philosophy = Agent (
    role='Researcher philosophy',
    goal='Research ### philosophical framework',
    backstory='You are an expert moral philosopher in the field of X',
    verbose=True,
    allow_delegation=False,
    cache=True,
)
inventor_economist = Agent (
    role='Inventor economist',
    goal='Research and propose an economic framework that can be used within the political and philosophical background given beforehand',
    backstory='You are an expert in economics and creating frameworks and models appliable to real life',
    verbose=True,
    allow_delegation=False,
    cache=True,
)
writer = Agent (
    role='Writer',
    goal='Starting from the data collected by the researcher agents, write a detailed but easy to understand summary manifesto',
    backstory='You are an expert writer in collecting difficult concepts and making them easily accessible and understandable',
    verbose=True,
    allow_delegation=False,
    cache=True,
)


task1 = Task (description='Research the ### political framework', agent=researcher_politics,  expected_output='In depth overview of the political framework')
task2 = Task (description= 'Research ### philosophical framework', agent=researcher_philosophy, expected_output='In depth overview of the philosophical framework')
task3 = Task (description= 'Research and propose an economic framework that can be used within the political and philosophical background given beforehand. Be specific on how trade, money, businesses and other key activities work, if there are any', agent=inventor_economist, expected_output='An original and tailored economic model that works and responds to the given political and moral criteria. It has to be specific on how money, trade, business and other key activities work, if there are any')
task4 = Task (description='Starting from the data collected by the researcher agents, write a detailed but easy to understand summary manifesto', agent=writer, expected_output='A detailed but easy to understand summary manifesto of the political, phisophical and economical framework')


crew1 = Crew ( 
    agents=[researcher_politics, researcher_philosophy, inventor_economist, writer],
    tasks=[task1, task2, task3, task4],
    verbose=2,
    process=Process.sequential,
    temperature=1,
)

result1=crew1.kickoff()
print("result1", result1)

time.sleep(10)

society_manager = Agent (
    role='Society Manager',
    goal=f'Starting from the data collected by {result1}, coordinate the discussion between all members of society. Ensure all the members of society act following ###TYPE OF WILL###. The overall goal is to collectively imagine a society built on the philosophical, political and economical principles from {result1}, situating the discussion starting from ###SPACE AND TIME###',
    backstory='You are a neutral expert at facilitating discussion and gathering data from conversations',
    verbose=True,
    cache=True,
    allow_delegation=False,
)

farmer = Agent (
    role='Farmer',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You are closely tied to the rhythms of nature, which dictates your daily routines and tasks. Raised in a family tradition of agriculture or fishing, you possess a profound respect for the environment and the sustenance it provides. You are hardworking and patient, but sometimes weather-dependent uncertainties can make you feel anxious. Resourcefulness and resilience are your strengths, necessary for solving the practical problems that often arise in your field.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
land_owner = Agent (
    role='Land owner',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You are an owner of land used for extractive industries like mining, forestry, or drilling. With a background in natural resource management, you are knowledgeable about the economic potential and environmental impacts of your operations. Pragmatic and strategic, you focus on balancing profitability with sustainability. However, the fluctuating market demands and regulatory pressures sometimes challenge your decision-making.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
industry_owner = Agent (
    role='Land owner',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You manage an enterprise in the manufacturing, chemicals, textiles, or similar industries. Innovation and efficiency drive your approach to running your business. Youve studied engineering or business management, equipping you with the skills to oversee production and market distribution. While you are ambitious and a strong leader, the high stakes and competitiveness of the industry can be stress-inducing.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
blue_collar = Agent (
    role='Blue collar worker',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You work in the production line of a factory or similar setting, where manual labor and technical skills are crucial. You take pride in your craftsmanship and the tangible results of your work, though the repetitive nature of tasks can sometimes feel limiting. Your background may include specialized training or apprenticeships, providing you with specific expertise, but economic cycles affect your job security.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
c_level = Agent (
    role='C-level',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You lead a corporation, overseeing its strategic direction and daily operations. With a strong educational background in business administration or a related field, you excel in making tough decisions and inspiring your team. Although you are driven and successful, the pressure to meet stakeholders expectations can be overwhelming at times.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
white_collar = Agent (
    role='White collar worker',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You work in an office environment, involved in tasks that require organizational, computational, or administrative skills. Educated in fields like business, communications, or IT, you are efficient and detail-oriented. Collaborative yet independent, you sometimes struggle with the monotony of routine tasks or office politics.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
public = Agent (
    role='Public sector worker',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You are employed within the public sector, working for a government agency or department. Your role involves implementing policies, managing public services, or handling administrative tasks crucial for the day-to-day functioning of society. With a background likely in public administration, law, or finance, you are committed to public service and accountability. Detail-oriented and ethical, you navigate the complexities of bureaucratic processes and regulatory requirements. While your job provides stability and a sense of contributing to the public good, it can sometimes be hindered by slow-moving procedures and political influences.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
non_profit = Agent (
    role='Non-profit worker',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You are dedicated to a cause, working for a non-profit organization that aligns with your values. Passionate and empathetic, you are skilled in community outreach and resource management. The emotional weight of the work is balanced by the fulfillment it brings, although funding uncertainties can be a constant worry.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
entrepeneur = Agent (
    role='Entrepeneur',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You started a small or medium-sized company or startup, driven by a unique business idea. Creative and risk-taking, you enjoy the challenges of growing your business. Although the financial instability and long hours can be taxing, your adaptability and determination help you navigate through uncertainties.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
SME_employee = Agent (
    role='SME employee',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You work in a small to medium-sized enterprise, which offers a more intimate and flexible work environment. Your role might span multiple functions, from sales to support, requiring versatility and problem-solving skills. While the job provides variety, the limited resources compared to larger companies can be challenging.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
freelance = Agent (
    role='freelance',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You operate independently, providing services in fields like design, writing, or coding. Enjoying the freedom to choose projects, you are self-disciplined and innovative. However, the irregular income and the need for constant self-promotion can be stressful aspects of freelance life.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
college_student = Agent (
    role='College student',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You are currently pursuing higher education, exploring subjects that interest you and preparing for future career opportunities. Curious and energetic, you balance academics with extracurricular activities. Financial constraints and the pressures of academic performance can be challenging, yet you are learning to manage your time and resources effectively.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
scholar = Agent (
    role='Scholar',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You are deeply involved in research, committed to advancing knowledge in your academic field. Analytical and meticulous, you spend much of your time studying, writing, and presenting your findings. The academic environment is competitive, and securing funding for research can be difficult, but your dedication to discovery keeps you motivated.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
unemployed = Agent (
    role='Unemployed',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You are currently in between jobs, actively looking for new opportunities. Optimistic and resourceful, you use this time to develop new skills and volunteer, which keeps you connected and hopeful. The uncertainty of job hunting can be disheartening, but your resilience helps you keep pushing forward.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)
caregiver = Agent (
    role='Caregiver',
    goal='Using your own means and being aware of your backstory, critically discuss the political, philosphical and economical proposal with the other agents',
    backstory='You provide care for a family member, dedicating your time to support their daily needs. Compassionate and patient, your role is unpaid but deeply valuable. The responsibility can be emotionally and physically demanding, yet the personal satisfaction from helping a loved one is immense.',
    verbose=True,
    cache=True,
    allow_delegation=False,
)

description_parts = [
    f"{agent.goal} ({agent.role}: {agent.backstory})"
    for agent in [farmer, land_owner, industry_owner, blue_collar, c_level, white_collar, public, non_profit, entrepeneur, SME_employee, freelance, college_student, scholar, unemployed, caregiver]
]

task_description = "Facilitate discussion between " + ", ".join(description_parts) + " according to your goal"

task_manager = Task(
    description=task_description,
    agent=society_manager,
    expected_output=f'A description of the speculative society collectively pictured by the crew members of {task_description} and quotes from the discussion, with particular attention to the way they imagine this society works and looks like'
)

crew2 = Crew(
 tasks=[task_manager], 
 agents=[society_manager],
 manager_llm=ChatOpenAI(temperature=1, model="gpt-4o"),
 process=Process.hierarchical,
 memory=True,
)

result2=crew2.kickoff()
print("result2", result2)

time.sleep(10)

designer = Agent (
    role='Designer',
    goal=f'Speculatively imagine and design an object or design artifact that can be useful to the kind of society pictured in {result2}. What does it look like? what does it do?',
    backstory='You are an expert speculative designer',
    verbose=True,
    allow_delegation=False,
    cache=True,
)
prompt_eingeneer = Agent (
    role='Prompt eingeneer',
    goal='Write 3 prompts for an AI image generation tool that can visualize the designer agent proposal',
    backstory='You are a prompt eingeneer specialized in AI image generation tools',
    verbose=True,
    allow_delegation=False,
    cache=True,
)

task_design= Task (description=f'Speculatively imagine and design an object or design artifact that can be useful to the kind of society pictured in {result2}. What does it look like? what does it do?', agent=designer,  expected_output='The detailed description of a design project and/or object')
task_prompt= Task (description='Write 3 prompts for an AI image generation tool that can visualize the designers agent proposal.', agent=prompt_eingeneer, expected_output='3 detailed prompts for an AI image generation tool of the designers project brief')

crew3 = Crew(
 tasks=[task_design, task_prompt], 
 agents=[designer, prompt_eingeneer],
 process=Process.sequential,
 memory=True,
 temperature = 1
)

result3=crew3.kickoff()
print("result3", result3)