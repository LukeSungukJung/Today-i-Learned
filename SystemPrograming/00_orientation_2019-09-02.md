<h2>시스템 프로그래밍</h2>
<div>
<h3>개요</h3>
<p>컴퓨터 프로그래밍은 추상화(abstraction)이 대부분이다. </p>
<h4>추상화의 예:</h4>
<ul>
<li>자료구조</li>
<li>가상메모리</li>
<li>스마트폰에 깔려있는 어플레이케이션 및 프로그램들 등</li>
</ul>
<p>그러나 시스템 내부의 동작에 대한 필요가 있거나, 몇몇 자원이나 메모리 오류로 인해 발생되는 버그들을 추상화라는 솔루션으로 해결하기엔 한계가 있다. 시스템 프로그래밍의 이해함으로써 기과한 버그를퇴치, 프레임 워크 내부에서 일어나는 일들에 대해서 알수 있고, 성능과 자원의 한계를 고려한 프로그래밍이 가능하다.
</p>
<h3>알아두고 가야 할것1</h3>
<h4>Memory OverFlow Problem</h4>
<p>*Rule:</p>
<ul>
	<li>Integer: 4byte(32 bits)</li>
	<li>Range: -2^31 ~ 2^31-1</li>
</ul>

<p><strong>Code</strong><br>
	void main(int argc, const char * argv[]) {<br>
    // insert code here...<br>
    float a = 1e20;<br>
    float b = -1e20;<br>
    float c = 3.14;<br>
    printf("%f \n",(a+b)+c);<br>
    printf("%f \n",a+(b+c));<br>
}<br>
</p>
<img src="c_res/mmoverflow.png"></img>
</div>