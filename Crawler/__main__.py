from myclass import *

@click.command()
@click.option('--url', default="", help='url of the user')
@click.option('--n', default=1, help='number of pages')
def main(url,n):

    p = Personne()
    p.user_info(url)
    dic=p.user_details
    p.user_posts(url+"/forums",n)
    dic1={"posts":p.data}
    dic.update(dic1)
    li=list(set(p.users_url))
    print(dic)
    print(li)
    save_data(dic,dic["name"],r"C:\Users\Hamza\Desktop\GameSpot_Crawler\GameSpot_Crawler\data\.")
    for e in li:
        try:
            p = Personne()
            p.user_info(e)
            dic=p.user_details
            p.user_posts(e+"/forums",n)
            dic1={"posts":p.data}
            dic.update(dic1)
            lj=list(set(p.users_url))
            for m in lj:
                try:
                    p = Personne()
                    p.user_info(m)
                    dic=p.user_details
                    p.user_posts(m+"/forums",n)
                    dic1={"posts":p.data}
                    dic.update(dic1)
                    save_data(dic,p.name,r"C:\Users\Hamza\Desktop\Facebook_Crawler\Facebook_Crawler\data\.")
                except:
                    pass
                
        except:
            pass
if __name__=='__main__':
    main()
