# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
#!pip -q install langchain openai
!pip show langchain
import os
os.environ["OPENAI_API_KEY"] = "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"
import pandas as pd

df = pd.read_csv('C:\Users\Eleon\Desktop\hopefully final\swiggy.csv')
!pip install langchain-experimental
!pip install --upgrade langchain-experimental
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent
from langchain.llms import OpenAI
agent = create_csv_agent(OpenAI(temperature=0), '/kaggle/input/swiggy-restuarant-dataset/swiggy.csv')
agent.agent.llm_chain.prompt.template
agent.run("how many customers are there?")
