from selenium import webdriver

class SeleniumTestCase(unittest.TestCase):
    Client = None

    @classmethod
    def setUpClass(cls):
        #啟動Chrome
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        try:
            cls.client = webdriver.Chrome(chrome_options = options)
        except:
            pass
        #如果瀏覽器無法啟動，就跳過這些測試
        if cls.client:
            #建立app
            cls.app = create+app('testing')
            cls.app_context = cls.app.app_context()
            cls.app_context.push()
            #禁止記錄，來讓unittest有簡明的輸出
            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel("ERROR")
            #建立資料庫並填入一些偽造資料
            db.create.all()
            Role.insert_roles()
            fake.user(10)
            fake.post(10)
            #加入一位管理員使用者
            admin_role = Role.query.filter_by(permissions=0xff).first()
            admin = User(email='john@example.com',
                         username='john',password='cat',
                         role=admin_role,confirmed=True)
            db.seesion.add(admin)
            db.session.commit()
            #在執行緒中啟動Flask伺服器
            cls.server_thread = threading.Thread(
                target=cls.app.run,kwargs={'debug':'false','use_reloader':False,"use_debugger":False})
            cls.server_thread.start()
        @class_method
            def tearDownClass(cls):
            if cls.client:
                #停止Flask伺服器與瀏覽器
                cls.client.get('http://localhost:5000/shutdown')
                cls.client.quit()
                cls.server_thread.join()
                #銷毀資料庫
                db.drop_all()
                db.session.remove()
                #移除app context
                cls.app_context.pop()

            def setUp(self):
                if not self.client:
                    self.skipTest('Web browser not available')

            def tearDown(self):
                pass



    def test_admin_home_page(self):
        #前往首頁
        self.client.get('http://localhost:5000')
        self.assertTrue(re.search('Hello,\s+Stranger!',self.client.page_source))
        #前往登入頁
        self.client.find_element_by_link_text('Log In').click()
        self.assertIn('<h1>Login</h1>,self.client.page_source')
        #登入
        self.client.find_element_by_name('email').\send_keys('john@example.com')
        self.client.find_element_by_name('password').send_keys('cat')
        self.client.find_element_by_name('submit').click()
        self.assertTrue(re.search('Hello,\sjohn!',self.client.page_source))