import os
from pprint import pprint

from requests import request

from ogr.services import pagure
from ogr.services.pagure import PagurePullRequest
from git import Repo

git_root = '/home/sakalosj/projects/test-projects/t1'
git_file = '/home/sakalosj/projects/test-projects/t1/test-file'
packit_token = os.getenv("PACKIT_CENTOS_TOKEN")
personal_token = os.getenv("PERSONAL_CENTOS_TOKEN")
pagure_personal_token = os.getenv("PERSONAL_PAGURE_TOKEN")


request_template = {
    'method': 'POST',
    # url : 'https://git.stg.centos.org/api/0/',
    # 'url': 'https://git.stg.centos.org/api/0/test1-jsakalos/pull-request/new',
    # 'params': None,
    # 'headers': {'Authorization': 'token T8X8RH6U430MWVYH9BA8LYEH1HMMHKMZDJ2035JZ7KAO4NCBK06D9BWB5X4BBKI0'},
    # 'data': {'title': 'ttt', 'branch_to': 'master', 'branch_from': 'master', 'initial_comment': 'bbb',
    #          'repo_from': 'test1-jsakalos', 'repo_from_username': 'sakalosj', 'repo_from_namespace': None},

}

request_template_packit_token = dict(**request_template, headers={'Authorization': 'token ' + packit_token})
request_template_my_token = dict(**request_template, headers={'Authorization': 'token ' + personal_token})
request_template_pagure_token = dict(**request_template, headers={'Authorization': 'token ' + pagure_personal_token})

new_project_packit_token = dict(**request_template_packit_token,
                                url='https://git.stg.centos.org/api/0/new',
                                data={'name': 'test2-jsakalos', 'description': 'desc'},
                                )

new_project_namespace_sourcegit_packit_token = dict(**request_template_packit_token,
                                                   url='https://git.stg.centos.org/api/0/new',
                                                   data={'name': 'test3-jsakalos', 'description': 'desc',
                                                         'namespace': 'source-git'},
                                                   )
new_project_my_token = dict(**request_template_my_token,
                                url='https://git.stg.centos.org/api/0/new',
                                data={'name': 'test2-jsakalos', 'description': 'desc'},
                                )

new_project_namespace_sourcegit_my_token = dict(**request_template_my_token,
                                                   url='https://git.stg.centos.org/api/0/new',
                                                   data={'name': 'test2-jsakalos', 'description': 'desc',
                                                         'namespace': 'source-git'},
                                                   )

new_pr_packit_token = dict(**request_template_packit_token,
                           url='https://git.stg.centos.org/api/0/test1-jsakalos/pull-request/new',
                           data={'title': 'ttt', 'branch_to': 'master', 'branch_from': 'master',
                                 'initial_comment': 'bbb',
                                 'repo_from': 'test1-jsakalos', 'repo_from_username': 'sakalosj',
                                 'repo_from_namespace': None},
                           )

new_pr_my_token = dict(**request_template_my_token,
                       url='https://git.stg.centos.org/api/0/fork/sakalosj/test1-jsakalos/pull-request/new',
                       data={'title': 'ttt', 'branch_to': 'master', 'branch_from': 'master', 'initial_comment': 'bbb',
                             'repo_from': 'test1-jsakalos', 'repo_from_username': 'sakalosj',
                             'repo_from_namespace': None},

                       )

new_pr_namespace_source_git_packit_token = dict(**request_template_packit_token,
                                                url='https://git.stg.centos.org/api/0/source-git/test2-jsakalos/pull-request/new',
                                                data={'title': 'ttt', 'branch_to': 'master', 'branch_from': 'master',
                                                      'initial_comment': 'bbb',
                                                      'repo_from': 'test1-jsakalos', 'repo_from_username': 'sakalosj',
                                                      'repo_from_namespace': 'source-git'},
                                                )

new_pr_namespace_source_git_packit_token2 = dict(**request_template_packit_token,
                                                url='https://git.stg.centos.org/api/0/source-git/test2-jsakalos/pull-request/new',
                                                data={'title': 'ttt', 'branch_to': 'master', 'branch_from': 'branch_a',
                                                      'initial_comment': 'bbb',
                                                      'repo_from': 'test2-jsakalos', 'repo_from_username': 'sakalosj',
                                                      'repo_from_namespace': 'source-git'},
                                                )

new_pr_namespace_source_git_my_token = dict(**request_template_my_token,
                                            url='https://git.stg.centos.org/api/0/test1-jsakalos/pull-request/new',
                                            data={'title': 'ttt', 'branch_to': 'master', 'branch_from': 'master',
                                                  'initial_comment': 'bbb',
                                                  'repo_from': 'test1-jsakalos', 'repo_from_username': 'sakalosj',
                                                  },
                                            )

comment = dict(**request_template_packit_token,
                                                 url='https://git.stg.centos.org/api/0/source-git/test2-jsakalos/pull-request/1/comment',
                                                 data={'comment': 'aaaaaaaaaaaaaa'},
                                                 )
comment_my = dict(**request_template_my_token,
               url='https://git.stg.centos.org/api/0/source-git/test2-jsakalos/pull-request/1/comment',
               data={'comment': 'aaaaaaaaaaaaaa'},
               )

fork = dict(**request_template_packit_token,
                  url='https://git.stg.centos.org/api/0/fork',
                  data={'repo': 'test3-jsakalos',
                        'namespace':'source-git',

                        },
                  )

flag_commit = dict(**request_template_packit_token,
            url='https://git.stg.centos.org/api/0/source-git/test2-jsakalos/c/71866f/flag',
            data={'username':'packit',
            'comment':'test flag',
                  'url':'https://test.tst',
                  'status':'pending'}
            )

flag_pr = dict(**request_template_pagure_token,
               url='https://pagure.io/api/0/packit-test/pull-request/2/flag',
               data={'username': 'packit',
                     'comment': 'test flag',
                     'url': 'https://test.tst',
                     'status': 'pending'}
               )

watch = dict(**request_template_packit_token,
            url='https://git.stg.centos.org/api/0/source-git/test2-jsakalos/watchers/update',
            data={'status':'3',
                  # 'username':'packit',
                  'watcher':'packit',
                  }
            )



def git_push(repo, message="test message"):
    try:
        repo.git.checkout("a")
        repo.git.add(update=True)
        repo.index.commit(message)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')


def update_file(file):
    with open(file, 'a') as f:
        f.write('.')


def new_commit():
    git_repo = Repo(git_root)
    update_file(git_file)
    git_push(git_repo)


service = pagure.PagureService(instance_url='https://git.stg.centos.org', token=packit_token)
service2 = pagure.PagureService(instance_url='https://git.stg.centos.org', token=personal_token)
ogr_project = service.get_project(repo='test1-jsakalos', namespace='source-git')


def manual_request(data):
    pprint(data)
    r = request(**data)
    pprint(r.content.decode())
    return r


def test_pagure_error():
    pr = service.get_project(repo="test1-jsakalos", namespace=None)
    pr.create_pr(title='test', body='body', target_branch='master', source_branch='a')




if __name__ == "__main__":
    # new_commit()
    pprint(ogr_project.get_owners())
    # pr = ogr_project.create_pr(title='test', body='body', target_branch='master', source_branch='a' )
    pr = ogr_project.get_pr(1)
    pr.comment('huraaaaa')
    # pr.merge()
    pr.close()
    # PagurePullRequest



