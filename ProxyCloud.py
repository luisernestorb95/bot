class ProxyCloud(object):
    def __init__(self, proxy):
        self.proxy = parse(proxy)
        print(self.proxy)
    def set_default (self,socket):
        self.default = socket
 
 
def parse(text):   
        proxy_tokens = text.split('://')
        print(proxy_tokens)
        type = proxy_tokens[0]
        print(type)
        da = proxy_tokens[1]
        de = da.split(':')
        ip = "//"+str(de[0])
        print(ip)
        port = de[1]
        print(port)
        
        return {'https':f'{type}://'+ip+':'+str(port)}

ProxyCloud("socks5://127.0.0.1:9050")