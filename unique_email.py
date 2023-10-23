#emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
def numUniqueEmails( emails: list[str]) -> int:
        re=set()
        for i in emails:
            local,domain=i.split('@')
            tem=""
            for c in local:
                if c==".": continue
                elif c=="+": break
                else: tem+=c
            re.add(tem+"@"+domain) 
        return len(re)