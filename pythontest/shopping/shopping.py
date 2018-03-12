import os
import sys
import csv
import datetime
import time
import types
from prettytable import PrettyTable
from prettytable import from_csv

#menu
def menu():
	
	menu='1输入工资  2商品列表  3购物  4购物车列表  5结账  6退出'
	print('\n'+menu)

#input salary
def salary_input():#input your salary
	global salary
	salary=int(input('Please putinto your salary a month:').strip());
	print('Your salary is',salary,' ￥ ')
	#print('salary>1000:',int(salary)>1000)
	print('')

def sale_table():#sale list
	print()
	print('商品表')
	goods_file=open('goods.csv','r')
	saletb=from_csv(goods_file)
	saletb.align='c'
	saletb.sort='goods'
	print(saletb)
	goods_file.close()
	
def shopping_cart():#shopping cart list
	print()	
	if os.path.getsize('shopping_cart.csv'):
		print('购物车列表：')
		shopping_file=open('shopping_cart.csv','r')
		shoppingtb=from_csv(shopping_file)
		shoppingtb.align='c'
		shoppingtb.sort='goods'
		print(shoppingtb)#print shopping_cart list
		shopping_file.close()
		
		list=[]
		with open('shopping_cart.csv','r') as shoppingcartfile:
			read=csv.reader(shoppingcartfile)
			sum=0
			global price_sum
			price_sum=0
			for line in read:
				list.append(line)
				#print('sum:',sum)
				#print(list[sum])
				if sum>0:
					price_sum=price_sum+int(list[sum][2])*int(list[sum][3])
				sum=sum+1
				#print('price_sum',price_sum)
				
		shoppingcartfile.close()
		print('购物总消费：',price_sum,'元')
		#print(type(list[2]))
		#print(list[2][1])
		now=datetime.datetime.now()
		print('购物时间：',now)
	else:
		print('购物车为空。')
		with open('shopping_cart.csv','w+') as shoppingcartfile:
			readcart=csv.reader(shoppingcartfile)
			shoppingcartfile.write("'编号','商品','单价￥','数量'")
			shoppingcartfile.flush()
		shoppingcartfile.close()
	
def shopping():#shopping
	#print(ifgoon,'')
	if ifgoon==True:
		ishopping=input('Would you going on shopping?(y/n):  ').strip()
		if ishopping=='y':
			print('I will shopping.')
			with open('goods.csv','r') as goodsfile:
				readgoods=csv.reader(goodsfile)
				listgoods=[]
				for linegoods in readgoods:
					listgoods.append(linegoods)
				with open('shopping_cart.csv','a+') as cartfilenow:
					readcart=csv.reader(cartfilenow)
					listcart=[]
					for linecart in readcart:
						listcart.append(linecart)
					print('listcart line is :',len(listcart))
					print(listcart)
					print('-----------')
					while True:
						shoppingNo=int(input('Plese input the goods NO. you want to buy: ').strip())
						shoppingNum=int(input('Plese input the goods NUM. you selected goods:  ').strip())
						listcart.append(listgoods[shoppingNo])
						listcart[-1].append('%d'%shoppingNum)
						print('-----',listcart)
						print('-------')
						for line in listcart:
							print(','.join(line))
							cartfilenow.write('\n'+','.join(line))
						
						#刷新购物车，再次显示购物车列表
						cartfilenow.flush()
						shopping_cart()
						
						isquit=input('Do you going on shopping?(y/n):   ').strip()
						
						if isquit=='n':
							cartfilenow.close()
							goodsfile.close()
							break
						
				cartfilenow.close()
			goodsfile.close()
	else:
		print('ifgoon=False')
	
def ifgoon():#estimate if going on shopping
	global ifgoon
	ifgoon==False
	
	list=[]
	with open('shopping_cart.csv','r') as shoppingcartfile:
		read=csv.reader(shoppingcartfile)
		sum=0
		global price_sum
		price_sum=0
		for line in read:
			list.append(line)
			#print('sum:',sum)
			#print(list[sum])
			if sum>0:
				price_sum=price_sum+int(list[sum][2])*int(list[sum][3])
			sum=sum+1
			#print('price_sum',price_sum)
			
	shoppingcartfile.close()	
	
	if price_sum<int(salary):
		ifgoon=True
		print('You can going on shopping?',ifgoon)
	else:
		print('You have no money to shopping')
	
def account():#结账
	
	input_a=input('Do you want to settle accounts?(y/n)  ').strip()
	if input_a=='y':
		shopping_cart()
		print('工资剩余： 工资(',salary,')-消费总额(',price_sum,')= ',int(salary)-int(price_sum),' ￥')
	elif input_a=='n':
		print()

def main():
	print('欢迎进入购物系统：')
	salary_input()#输入工资
	while True:
		print('------------------------------------------------------')
		menu()#购物菜单
		inputnum=int(input('Please input the NUM. which you want:').strip())#输入购物菜单编号
		if inputnum==1:
			salary_input()
		elif inputnum==2:
			sale_table()
		elif inputnum==3:
			ifgoon()
			shopping()
		elif inputnum==4:
			shopping_cart()
			#ifgoon()
			#shopping()
		elif inputnum==5:
			account()
		elif inputnum==6:
			print('谢谢光临！')
			break
	

main()