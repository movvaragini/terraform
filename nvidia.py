from urllib.request import Request, urlopen
import json
from jinja2 import Template

def get_commit_details(base_url, user, repo, branch):
        if base_url!='' and user!='' and repo!='' and branch!='':
            url = '{base_url}/repos/{user}/{repo}/commits?per_page=1/{branch}'.format(
                base_url=base_url, user=user, repo=repo,branch=branch)
            req = Request(
                url,
                data=None,
                headers={
                    'User-Agent': 'terraform by github.com/movvaragini/terraform'
                }
            )
            response = urlopen(req)
            data=json.loads(response.read().decode('utf-8'))
            lastest_five_commits=data[:5]
            count = 0
            for element in lastest_five_commits:

                count += 1
                commit_obj=convert_dict(element)
                print(commit_obj)

                rendered_data=rendering(commit_obj)
                copy_data(rendered_data)
            if count!=0:
                return True
            else:
                return False

def convert_dict(data):
    sha= data['sha']
    author=data['commit']['author']['name']
    message=data['commit']['message']
    commit_obj={'sha':sha, 'author':author, 'message':message}
    return commit_obj

def rendering(commit_obj):
    t = Template('''
    <html>
      <body>
        <table border="1">
          <tr>
            <td>{% for key, value in dict_item.items() %} {{value}}\n{% endfor %}</td>
          </tr>
        </table>
      </body>
    </html>
    ''')
    rendered_data = t.render(dict_item=commit_obj)
    return rendered_data

def copy_data(commit_obj):
    with open("nvidia.html", "a") as text_file:
        text_file.writelines("%s" % commit_obj)

if __name__ == '__main__':
    # base_url='https://api.github.com'
    base_url=input('Enter base_url of github: ')
    user=input('Enter user of github: ')
    repo=input('Enter repo of github: ')
    branch=input('Enter branch of github: ')
    get_commit_details(base_url, user, repo, branch)
