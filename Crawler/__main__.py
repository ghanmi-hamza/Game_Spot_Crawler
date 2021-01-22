from myclass import *

@click.command()
@click.option('--url', default="", help='url of the user')
@click.option('--n', default=1, help='number of pages')
@click.option('--nb_images', default=1, help='number of profile images')
@click.option('--pubs', default="False", help='get publication or not')
@click.option('--download', default="False", help='download data or not')
def main(url,n,pubs,nb_images,download):

    p = GamespotDriver()
    p.get_user_info(url,nb_images)
    dic=p.user_details
    if pubs=="True":
        p.get_publications(url+"forums",n)
        dic1={"posts":p.data}
        dic.update(dic1)
    print(dic)
    if download=="True":
        save_data(dic,dic["name"],r"C:\Users\Hamza\Desktop\GameSpot_Crawler\GameSpot_Crawler\data\.")
    
if __name__=='__main__':
    main()
