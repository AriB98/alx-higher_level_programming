
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Test __str__ return value """
        r1 = Square(3, 2, 5, 3)
        res = "[Square] (3) 2/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.size = 11
        res = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Test __str__ return value """
        s1 = Square(5)
        res = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s2 = Square(3, 7, 1)
        res = "[Square] (2) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), res)

        s3 = Square(1, 1, 1)
        res = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Test __str__ return value """
        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3"
        self.assertEqual(s1.__str__(), res)

    def test_display_3(self):
        """ Test string printed """
        s1 = Square(5, 2, 1)
        res = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Test string printed """
        s1 = Square(3)
        res = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

        s1.x = 1
        res = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

        s1.y = 2
        res = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_update(self):
        """ Test update method """
        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_2(self):
        """ Test update method """
        s1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_3(self):
        """ Test update method """
        s1 = Square(1)
        res = "[Square] (1) 0/0 - 1\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(2, 2, 2, 2)
        res = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(y=3)
        res = "[Square] (2) 2/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s1.update(id=1, size=10)
        res = "[Square] (1) 2/3 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_4(self):
        """ Test update method """
        s1 = Square(10)
        res = "[Square] (1) 0/0 - 10\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        dic = {'size': 3, 'y': 5}
        s1.update(**dic)
        res = "[Square] (1) 0/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_5(self):
        """ Test update method """
        s1 = Square(7)
        res = "[Square] (1) 0/0 - 7\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        dic = {'id': 10, 'x': '5', 'y': 5}

        with self.assertRaises(TypeError):
            s1.update(**dic)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        s1 = Square(1, 2, 3)
        res = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        s1 = Square(2, 2, 2)
        res = "[Square] (1) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

        s2 = Square(5)
        res = "[Square] (2) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s2)
            self.assertEqual(str_out.getvalue(), res)

        s1_dictionary = s1.to_dictionary()
        s2.update(**s1_dictionary)

        self.assertEqual(s1.width, s2.width)
        self.assertEqual(s1.height, s2.height)
        self.assertEqual(s1.x, s2.x)
        self.assertEqual(s1.y, s2.y)
        self.assertEqual(s1.id, s2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """
        s1 = Square(2)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_json_file(self):
        """ Test Dictionary to JSON string """
        s1 = Square(2)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())
        res = res.replace("'", "\"")

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res)

        Square.save_to_file([s1])
        res = "[{}]".format(dictionary.__str__())
        res = res.replace("'", "\"")

        with open("Square.json", "r") as file:
            res2 = file.read()

        self.assertEqual(res, res2)

    def test_value_square(self):
        """ Test value pased to Square """
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1, 'x': 2}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_load_from_file_2(self):
        """ Test load JSON file """
        s1 = Square(5)
        s2 = Square(8, 2, 5)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
