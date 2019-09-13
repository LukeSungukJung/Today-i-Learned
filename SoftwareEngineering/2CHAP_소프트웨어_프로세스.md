<h3>소프트웨어 개발 프로세스</h3>
<ul>
	<li>플젝을 소뮤고 작업으로 구성하는 일반적인 접근 방법</li>
	<li>관리자와 팀원들이 다음사항을 결정하는데 도움- 무엇을 해야할지 어떤순서로 해야할지</li>
	<li>모델은 작업 방식을 엄격하게 규정하기보다 생각하는 도움을 주어야댐</li>
	<li>각 플젝은 고유의 계획을 가지고 진행되어야댐</li>
</ul>

<h3>즉흥적인 개발 프로세스</h3>
<p>좋은 엔지니어링 과정을 따르지 않았을때 발생하는 문제들</p>
<ul>
	<li>구현하기 전에 요구나 설계 등의 중요성 인식X</li>
	<li>설계가 잘되지 않는 다면 소프트웨어의 질이 떨어질수 있음</li>
	<li>체계적인 테스트나 품질 보증 같은 작업의 필요성 간과</li>
	<li>위의 이유들로 개발과 유지보수 비용이 비싸짐</li>
</ul>
<table>
	<thead>
		<tr>
			<th>프로그래밍 -></th>
			<td> 만족할 때까지 수정 <-~-></td>
			<td>개선을 위한 아이디어 도</td>
		</tr>
	</thead>
</table>


<h3>대표적인 소프트웨어 개발 프로세스 모델</h3>
<p><strong>중요한 모델</strong></p>
<ul>
	<li>폭포수 모델</li>
	<li>점증적 모델</li>
	<li>나선형 모델</li>
	<li>진화적 모델</li>
	<li>애자일 모델</li>
</ul>


<h3>폭포수 모델</h3>
<table>
	<thead>
		<tr>
			<td>요구사항 정의</td>
			<td>V & V( Validation & Verifitcation ) </td>
			<td>ㄱ</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>ㄴ</td>
			<td>명세화</td>
			<td>V & V( Validation & Verifitcation ) </td>
			<td>ㄱ</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
		</tr>
		<tr>
			<td>-</td>
			<td>ㄴ</td>
			<td>디자인</td>
			<td>V & V( Validation & Verifitcation ) </td>
			<td>ㄱ</td>
			<td>-</td>
			<td>-</td>
		</tr>
		<tr>
			<td>-</td>
			<td>-</td>
			<td>ㄴ</td>
			<td>구현</td>
			<td>V & V( Validation & Verifitcation ) </td>
			<td>ㄱ</td>
			<td>-</td>
		</tr>
		<tr>
			<td>-</td>
			<td>-</td>
			<td>-</td>
			<td>ㄴ</td>
			<td>통합 및 배포</td>
			<td>V & V( Validation & Verifitcation ) </td>
			<td>ㄱ</td>
		</tr>
		<tr>
			<td>-</td>
			<td>-</td>
			<td>-</td>
			<td>-</td>
			<td>ㄴ</td>
			<td>유지보</td>
			<td>V & V( Validation & Verifitcation ) </td>
		</tr>
	</tbody>
</table>
<p>특징</p>
<ul>
	<li>각 단계가 다음 단계 시작전에 끝나야댐</li>
	<li>순서적: 각 단계 사이에 중복이나 상호작용이 없음</li>
	<li>각단계의 결과는 다음단계가 시작되기전에 점검</li>
	<li>바로 전단계로 피드백</li>
</ul>
<p>적용</p>
<ul>
	<li>대규모 공학 플젝에 주로 사용됨</li>
	<li>요구사항을 잘 이해하고 있거나 변경이 한정적인 상황에 적합</li>
</ul>
<p>단점</p>
<ul>
	<li>초기 단계 강조로 인해 코딩 및 테스트 지연</li>
	<li>각 단계 전환에 많은 노력이 필요</li>
	<li>프로토 타입과 재사용의 기회가 줄어</li>
	<li>소용없는 다수의 문서를 생산할 가능성이 있</li>
</ul>

<h3>폭포수 모델</h3>
<p>
	빠른 시간안에 시장에 출시하여야 하는 경우 : 시장 독점을 위</br>
	이를 위해 시스템을 나누어 릴리즈
</p>
<ul>
	<li>1. 베이스 모델 출시</li>
	<li>2. 요구에 따라 부가 서비스 출시</li>
	<li>3. 2에 이어 계속 추가하여 출시</li>
</ul>
<table>
	<tbody>
		<tr>
			<td rowspan="3" colspan="4">⌈-> (phase 1)</td>
			<td>디자인</td>
			<td>V & V</td>
			<td>ㄱ</td>
			<td>-</td>
		</tr>
		<tr>	
			<td>ㄴ</td>
			<td>구현</td>
			<td>V & V</td>
			<td>ㄱ</td>
		</tr>
		<tr>
			<td>-</td>
			<td>ㄴ</td>
			<td>통합 및 배포 </td>
			<td>V & V</td>
		</tr>
		<tr>
			<td>요구사항 정의</td>
			<td>V & V</td>
			<td>ㄱ</td>
			<td>-</td>
			<td colspan="4" rowspan="3">-</td>
		</tr>
		<tr>
			<td>ㄴ</td>
			<td>명세화</td>
			<td>V & V</td>
			<td>ㄱ</td>
		</tr>
		<tr>
			<td>-</td>
			<td>ㄴ</td>
			<td>계획(플래닝)</td>
			<td>V & V</td>
		</tr>
		<tr>
			<td rowspan="4" colspan="4">ㄴ-> (phase 2)</td>
			<td>디자인</td>
			<td>V & V</td>
			<td>ㄱ</td>
			<td>-</td>
		</tr>
		<tr>
			<td>ㄴ</td>
			<td>구현</td>
			<td>V & V</td>
			<td>ㄱ</td>
		</tr>
		<tr>
			<td>-</td>
			<td></td>
			<td>통합 및 배포 </td>
			<td>V & V</td>
		</tr>
	</tbody>
</table>

<p>
	릴리즈 구성 방법
</p>
<ul>
	<li>- 점증적 방법 : 기능별로 릴리즈</li>
	<li>- 반복적 방법 : 릴리즈 할때마다 기능의 완성도를 높임</li>
</ul>
<p>
	단계적 개발
</p>
<ul>
	<li>기능이 부족하더라도 초기에 사용 가능, 교육 가능</li>
	<li>처음에 시장에 출시된 sw는 시장을 빨리 형성가능(독점가능)</li>
	<li>자주 릴리즈 하면 가동중인 시스템에서 예상치 못한 문제를 발견 및 해결 가능</li>
	<li>개발 팀이 릴리즈 마다 다른 전문 영역에 초점을 둘수 있</li>
</ul>

