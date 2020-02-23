var jsbg1 = document.getElementById("bg1")
var jsbg2 = document.getElementById("bg2")
var airplane = document.getElementById("airplane")
var mainSrceen = document.getElementById("mainSrceen")
//加载音乐
var musicBackground = document.getElementById("musicBackground")
var musicBullet = document.getElementById("musicBullet")
var musicTank = document.getElementById("musicTank")
var musicOver = document.getElementById("musicOver")

var start = document.getElementById("start")
var timer = document.getElementById("timer")
var conunt = document.getElementById("count")
var scoring = document.getElementById("scoring")
var end = document.getElementById("end")

timerNum = 0
start.addEventListener("mousedown",function(){
	var time = setInterval(function(){
		timerNum += 1
		timer.textContent = timerNum + "/s"
	},1000)
	start.textContent = ""
},false)



//背景音乐
var tiemrMusicBackground = setInterval(function(){
	musicBackground.src = "img/game_music.mp3"
},48000)


//背景动起来
var timerBG = setInterval(function(){
	jsbg1.style.top = jsbg1.offsetTop + 1 + "px"
	jsbg2.style.top = jsbg2.offsetTop + 1 + "px"
	if (jsbg1.offsetTop >= 768){
		jsbg1.style.top = "-768px"
	}
	if (jsbg2.offsetTop >= 768){
		jsbg2.style.top = "-768px"
	}
},10)

//飞机移动
airplane.addEventListener("mousedown",function(e){
	if (start.textContent != ""){
		return false
	}
	var ev = e || window.event
	basex = ev.pageX
	basey = ev.pageY
	
	movex = 0
	movey = 0
	
	//主屏幕移动事件
	mainSrceen.addEventListener("mousemove", function(e){
		var en = e || window.event
		movex = en.pageX - basex
		basex = en.pageX
		movey = en.pageY - basey
		basey = en.pageY
		
		airplane.style.left = airplane.offsetLeft + movex + "px"
		airplane.style.top = airplane.offsetTop + movey + "px"
	},false)
	
	
},false)

//发射子弹
var timerBullet = setInterval(function(){
	if (start.textContent != ""){
		return false
	}
	
	//创建子弹
	var bullet = document.createElement("div")
	mainSrceen.appendChild(bullet)
	bullet.className = "bullet"
	bullet.style.left = airplane.offsetLeft + 51.5 +"px"
	bullet.style.top = airplane.offsetTop  - 10 + "px"
	musicBullet.src = "img/bullet.mp3"
	
	//让子弹飞
	var timerBulletFly = setInterval(function(){
		bullet.style.top = bullet.offsetTop - 10 + "px"
		if (bullet.offsetTop <= -20){
			clearInterval(timerBulletFly)
			mainSrceen.removeChild(bullet)
		}
	},50)
	bullet.timer = timerBulletFly
	
},1000)

//敌人下落
var timerTank = setInterval(function(){
	if (start.textContent != ""){
		return false
	}
	//创建坦克
	var tank = document.createElement("div")
	mainSrceen.appendChild(tank)
	tank.className = "tank"
	tank.style.top = "0px"
	tank.style.left = randomNum(0, 472) + "px"
	
	//让坦克飞
	var timerTankFly = setInterval(function(){
		tank.style.top = tank.offsetTop + 10 + "px"
		if (tank.offsetTop >= 768){
			clearInterval(timerTankFly)
			mainSrceen.removeChild(tank)
		}
	},50)
	tank.timer = timerTankFly
	
},1000)

//随机数
function randomNum(min, max){
	return parseInt(Math.random() * (max - min) + min)
}

//检测是否发生(矩形)碰撞
	function pzjcFunc(obj1, obj2){
		var obj1Left = obj1.offsetLeft;
		var obj1Width = obj1Left + obj1.offsetWidth;
		var obj1Top = obj1.offsetTop;
		var obj1Height = obj1Top + obj1.offsetHeight;

		var obj2Left = obj2.offsetLeft;
		var obj2Width = obj2Left + obj2.offsetWidth;
		var obj2Top = obj2.offsetTop;
		var obj2Height = obj2Top + obj2.offsetHeight;
			

		if ( !(obj1Left > obj2Width || obj1Width < obj2Left || obj1Top > obj2Height || obj1Height < obj2Top) ) {
			return true
		} else {
			return false
		}
	}

//碰撞检测
var timerPZJC = setInterval(function(){
	var allTanks = document.getElementsByClassName("tank")
	var allBullets = document.getElementsByClassName("bullet")
	for (var i = 0; i < allBullets.length; i++){
		for (var j = 0; j < allTanks.length; j++){
			var b = allBullets[i]
			var t = allTanks[j]
			
			if (pzjcFunc(b, t)){
				musicTank.src = "img/enemy3_down.mp3"
				clearInterval(b.timer)
				clearInterval(t.timer)
				mainSrceen.removeChild(b)
				mainSrceen.removeChild(t)
				conunt.textContent = parseInt(conunt.textContent) + 1
				scoring.textContent = parseInt(scoring.textContent) + randomNum(1,10)
				break
			}
		}
	}
},50)

//死亡检测
var timerDie = setInterval(function(){
	var allTanks = document.getElementsByClassName("tank")
	for (var i = 0; i < allTanks.length; i++){
		if (pzjcFunc(allTanks[i], airplane)){
			for (var j = 0; j < 1000; j++){
				musicOver.src = "img/game_over.mp3"
				clearInterval(j)
			}
			end.style.top = "333px"
			end.textContent = "用时：" + timer.textContent + "累积击落"+ conunt.textContent + "量坦克" + "获得：" + scoring.textContent + "分"
			break
		}
	}
},50)