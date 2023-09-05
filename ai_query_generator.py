import os
import json

import requests


url = 'https://api.openai.com/v1/completions'
#api_key = os.environ.get('open_ai_api_key')
api_key='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'




if api_key is None:
    raise Exception('Please provide OpenAI API key')

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {api_key}'
}


def generate_query(problem):
    payload = json.dumps({
      'model': 'text-davinci-003',
       'prompt': 'Table profile_details is available with the columns id,emp_id,name,email,gender,experience,'
                'designation,tools,area_of_interest.\n'
                'Sample data in the table-\n'
                '1,111,Willow Floyd,wfloyd0@msn.com,Female,6,Software Developer,"Java, mysql, Nodejs",React\n'
                '2,2,Niels Klimek,nklimek1@un.org,Male,2,Associate Software Developer,Figma,React\n'
                '3,234,Dario Treasaden,dtreasaden2@hao123.com,Male,4,Software Developer,"Java, kafka,c#",Node.js\n'
                '4,4,Deck Desaur,ddesaur3@wunderground.com,Male,13,Architect,"Java, mysql, nosql, kafka",C++\n'
                '5,5,Steward Billie,sbillie4@live.com,Male,8,Senior Software Developer,"PHP,SQL",Python\n'
                '6,6,Waly McQuaid,wmcquaid5@home.pl,Genderqueer,6,Software Developer,"MongoDB,React",C++\n'
                '7,7,Danya Rable,drable6@bizjournals.com,Genderfluid,8,Senior Software Developer,"Go,PHP",HTML\n'
                '8,8,Flore Toy,ftoy7@xrea.com,Female,2,Associate Software Developer,Python,CSS\n'
                '9,9,Berkeley Vittori,bvittori8@zdnet.com,Male,4,Software Developer,ASP.NET,React\n'
                '10,6767,Onida De Rechter,ode9@wp.com,Female,4,Software Developer,"Express.js, Nodejs",Python\n'
                '11,11,Kathrine Ricardou,kricardoua@lycos.com,Female,1,Associate Software Developer,"PHP, Python",React\n'
                '12,12,Pate Turbefield,pturbefieldb@xinhuanet.com,Bigender,8,Senior Software Developer,Java,SQL\n'
                '13,13,Lida McKyrrelly,lmckyrrellyc@mayoclinic.com,Female,3,Software Developer,JavaScript,JavaScript\n'
                '14,14,Odetta Tellenbrok,otellenbrokd@g.co,Female,12,Development Lead,"MongoDB, JS, Nodejs",Git\n'
                '15,1234,Durand Bartlett,dbartlette@samsung.com,Male,1,Associate Software Developer,Go,CSS\n'
                '16,16,Tamara O Murtagh,tomurtaghf@state.tx.us,Female,13,Architect,"Java, SQL, Python",C++\n'
                '17,17,Avivah Massei,amasseig@weibo.com,Female,10,Senior Software Developer,"SQL, Nodejs, React",React\n'
                '18,18,Merrill Lourenco,mlourencoh@example.com,Non-binary,10,Senior Software Developer,"SQL, Nodejs,c#",React\n'
                '19,1212,Darwin Smowton,dsmowtoni@wix.com,Male,9,Senior Software Developer,"Swift, MongoDb, Laravel",Java\n'
                '20,20,Emmalyn Byrcher,ebyrcherj@i2i.jp,Female,8,Senior Software Developer,"Python, Android, Django",HTML\n'
                '21,21,Guillemette Bleasdale,gbleasdalek@instagram.com,Female,1,Associate Software Developer,"C++, HTML",React\n'
                '22,22,Matti Cassedy,mcassedyl@xinhuanet.com,Female,11,Development Lead,"C++, Java",SQL\n'
                '23,1245,Bobbee Francais,bfrancaism@surveymonkey.com,Female,11,Development Lead,"Ruby, Spring",React\n'
                '24,24,Urbanus Gall,ugalln@eventbrite.com,Male,14,Architect,"SQL, ios, PHP",JavaScript\n'
                '25,25,Del Borles,dborleso@usatoday.com,Female,9,Senior Software Developer,"SQL, Kafka, Nodejs",Node.js\n'
                '26,26,Adah O Cuolahan,aop@ning.com,Female,14,Architect,CSS,Node.js\n'
                '27,4567,Alfons Rammell,arammellq@chronoengine.com,Male,3,Software Developer,"Node.js, React",Node.js\n'
                '28,28,Claiborne Cussons,ccussonsr@usatoday.com,Male,5,Software Developer,"Node.js, React",Node.js\n'
                '29,29,Maurits Theodoris,mtheodoriss@parallels.com,Male,13,Architect,"Angular, Java",C++\n'
                '30,30,Clyde Flintoft,cflintoftt@devhub.com,Male,2,Associate Software Developer,Django,CSS\n'
                '31,1317,Nixie Brome,nbromeu@ox.ac.uk,Female,3,Software Developer,Ruby,Git\n'
                '32,32,Jo-anne Iannuzzelli,jiannuzzelliv@ning.com,Female,2,Associate Software Developer,"CSS, HTML, JQuery",Python\n'
                '33,33,Alaster MacMickan,amacmickanw@wikispaces.com,Male,9,Senior Software Developer,"Express.js, Nodejs",HTML\n'
                '34,34,Gabbie Gurko,ggurkox@census.gov,Female,13,Architect,Laravel,Python\n'
                '35,35,Jobie Ramsby,jramsbyy@naver.com,Genderfluid,13,Architect,"Vue.js, React",Git\n'
                '36,36,Alaine Geraldi,ageraldiz@auda.org.au,Female,10,Senior Software Developer,PHP,HTML\n'
                '37,4566,Chrotoem Cholwell,ccholwell10@slashdot.org,Male,8,Senior Software Developer,"Vue.js, React",Git\n'
                '38,38,Nefen Ninnoli,nninnoli11@disqus.com,Male,11,Development Lead,Ruby,Node.js\n'
                '39,39,Gawain Hanway,ghanway12@salon.com,Male,14,Architect,"CSS, HTML,Angular",Git\n'
                '40,40,Merill Killelay,mkillelay13@wikia.com,Male,13,Architect,Spring,JavaScript\n'
                '41,41,Salim Gantzman,sgantzman14@wisc.edu,Male,8,Senior Software Developer,Django,Node.js\n'
                '42,42,Gracia Inett,ginett15@theguardian.com,Female,5,Software Developer,React,C++\n'
                '43,7890,Rufus Suscens,rsuscens16@eventbrite.com,Male,11,Development Lead,HTML,HTML\n'
                '44,44,Viviene De Beauchemp,vde17@senate.gov,Female,9,Senior Software Developer,"Vue.js, React",CSS\n'
                '45,45,Hailee Zimmerman,hzimmerman18@microsoft.com,Female,12,Development Lead,C#,Git\n'
                '46,46,Donal Schiesterl,dschiesterl19@oracle.com,Male,5,Software Developer,"CSS, HTML, REACT",Python\n'
                '47,47,Livia Pittet,lpittet1a@xinhuanet.com,Female,10,Senior Software Developer,Ruby,C++\n'
                '48,48,Jean Lavender,jlavender1b@mozilla.org,Male,3,Software Developer,Vue.js,Python\n'
                '49,49,Lalo Spowart,lspowart1c@phpbb.com,Male,13,Architect,Laravel,React\n'
                '50,3,Joly Armall,jarmall1d@uol.com.br,Female,9,Senior Software Developer,Node.js,Java\n'
                'Generate only single line Postgres query to give all data about the person(s) who might\n'
                'be able to solve the following problem-\n'
                f'"{problem}".\n'
                'The column area_of_interest has the area the person is particularly interested in, and the column '
                'tools has the tools/technologies/databases/frameworks on which the'
                'person has worked. Even if someone is not particularly interested in something, but has worked'
                'in that area, they can help with it. Search should be case insensitive.'
                'Do not generate query and return the message "Data not available" if appropriate columns are not '
                'available in the table. The person who can help the most should be on top.',
      'max_tokens': 250,
      'temperature': 0
    })

    response = requests.request('POST', url, headers=headers, data=payload)

    if response.status_code == 200:
        query = json.loads(response.text)['choices'][0]['text']
    else:
        query = None

    return query


def main():
    print(generate_query('I am new to Python, and am having trouble with a script'))


if __name__ == '__main__':
    main()
