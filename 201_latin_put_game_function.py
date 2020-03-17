if __name__ == "__main__":
 class change:
      def latin_put(self, str):
          if str[0] in ["a", "i", "e", "o", "u"]:
             print(str+"ay")
          else:
            print(str[1:]+str[0]+"ay")

y = change()
y.latin_put("ram")