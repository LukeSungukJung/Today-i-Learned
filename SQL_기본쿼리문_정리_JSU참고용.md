
<h1>SQL 쿼리문 기본 정리</h1>

<h3>컬럼의 종류</h3>

<table>
	<thead>
		<tr>
			<td>데이터 유형</td>
			<td>설명</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Varchar</td>
			<td>Character varying의 약자로 가변 길이의 문자열 정보임 sql의 경우 최대 8000바이트 저장 가능</td>
		</tr>
		<tr>
			<td>NUMERIC</td>
			<td>정수, 실수 등 숫자 정볼르 가지고 있음 표기법의 예로 정수부분이 6자리 소수점이 2자리인것을 표현하면 NUMERIC(8,2)로 표기하면 된다.</td>
		</tr>
			<tr>
			<td>DATE</td>
			<td>날짜와 시간정보 관리함</td>
		</tr>
	</tbody>
	</table>
<div>
<h3>제약 조건의 종류</h3>

<ul>
	<li>PRIMARY KEY(기본키) : 기본키 중복안되고, NULL입력 안됨. </li>
	<li>UNIQUE KEY(고유키) : NULL있어도 됨, 다만 중복만 안됨</li>
	<li>NOT NULL : 무조건 비우면 안됨 'DEFAULT'설정이 되어있으면, 새로운 로 추가시 아무값입력안하면 디폴트 세팅이 들어감</li>
	<li>CHECK :  TRUE FALSE로 평가 할수 있는 논리식 지정</li>
	<li>FOREIGN KEY(외래키) : 다른 테이블과의 관계를 정의하기위해 기본키를 다른 테이블의 왜리키로 복사하는 경우의 복사된 기본키를 지칭함.</li>

</ul>
</div>

<div>
<h3>SQL 문장들의 종류</h3>

<ul>
	<li><a  href="#dml">DML: 데이터 조작어 -[SELECT, INSERT, UPDATE, DELETE]</a></li>
	<li><a  href="#ddl">DDL: 데아터 정의어 -[CREATE, ALTER DROP, RENAME]</a></li>
	<li><a  href="#dcl">DCL: 데이터 제어어 -[GRANT, REVOKE]</a></li>
	<li><a  href="#tcl">TCL: 트랜잭션 제어어 -[COMMIT, ROLLBACK]</a></li>

</ul>
</div>

<div id="dml">
<h3>DML</h3>
<ul>
	<li>INSERT (syntax) - INSERT INTO 테이블명 (컬럼리스트) VALUES(값1,값2,....) :  테이블에 넣을 컬럼을 정의해주고 그 컬럼을 채울 값들을 입력해준후 새로운 행을 추가함.</li>
	<li>UPDATE (syntax)- UPDATE TABLE tablename  SET 컬럼명 = 새로운 값  : 테이블에 컬럼 명 제거</li>
	<li>DELETE (syntax)- DELETE [FROM] tablename : 테이블의 정보가 필요 없게 되었을 경우 데이터 삭제를 수행함 where 절로 어디 조질지 위치 지정가능. 암것도없이 그냥 저대로 쓰면 테이블 전체 데이터가 삭제댐</li>
	<li>SELECT (syntax)- SELECT [ALL/DISTINCT] 보고싶은 컬럼명1,2,3... FROM 테이블명;  : 테이블에서 보고싶은 컬럼명을 보여줌 ALL-디폴트로 중복데이터도 다보여줌, DISTINCT - 중복데이터는 제거해서 보여줌  *(와일드카드) 사용시 전체 보여줌, 좌측정렬: 문자 및 날짜 데이터, 우측정렬: 숫자 데이터</li>
	<li>ALIAS (syntax) 컬럼명 as 별명, 컬럼명2 as 별명2,... : 조회된 데이터에 별명을 부과해서 컬럼 레이블을 변경 가능함.  ALIAS는 컬럼명 바로 뒤에 오고, 특수문자 공백  대소문자구분이 필요할 경우 사용됨. 별명에 공백이 들어갈경우 "",'',[]를 써야댐 "선수 이름" 등 이런식으로 지정해줘야댐</li>
</ul>
<h4>산술 연산자</h4>
<p>+,-,/,* 우리가 아는 그 연산자 예시: select 몸무게+ 키 as "몸무게 더하기 키" from 선수들로 하면 각 로우의 몸무게 + 키 값을 더한것을 앨리어스로 해서 계산한 값을 보여줌</p>
<h4>합성 연산자</h4>
<p>문자와 문자를 연결하는 합성 연산자를 사용하면 별도의 프로그램 도움 없이도 sql 문장가지고만 유용한 리포트를 출력 가능하다.</p>
<ul>
	<li>문자와 문자를 연결하는 경우 2개의 수직 바(||)에 의해 이루어진다.(오라클)</li>
	<li>문자와 문자를 연결하는 경우 '+'에 의해 이루어진다.(sql server)</li>
	<li>두 벤더 모두 공통적으로 CONCAT(str1,str2)를 이용해서 연결 가능하다.</li>
	<li>컬럼과 문자 또는 다른 컬럼과 연결 시킬수도 있음.</li>
	<li>문자 표현식의 결과에 의해 새로운 칼럼을 생성한다.</li>	
</ul>
<h4>Where절</h4>
<p>where : 보통 select * from 테이블 where 조건식 으로 select 문에 끼어서 조건을 부여해서 찿고자하는 조건을 부과해서 사용자가 보여주고 싶은 정보만 선택적으로 보여주게 한다.</p>
<p>조건식의 내용</p>
<ul>
	<li>칼럼(Column)명 </li>
	<li>비교 연산자</li>
	<li>문자, 숫자, 표현식</li>
	<li>비교 칼럼명(JOIN 사용시)</li>
</ul>
<table>
	<thead>
		<tr>
			<td>구분</td>
			<td>연산자</td>
			<td>연산자의 의미</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td rowspan="3">비교 연산자</td>
			<td>=</td>
			<td>같다</td>
		</tr>
		<tr>
			<td>>,>=</td>
			<td>크다,크거나 같다</td>
		</tr>
		<tr>
			<td><,<=</td>
			<td>작다,작거나 같다</td>
		</tr>
		<tr>
			<td rowspan="4">SQL 연산자</td>
			<td>BETWEEN a AND b</td>
			<td>a와 b의 값 사이에 있으면 된다. (a,b 포함)</td>
		</tr>
		<tr>
			<td>IN(list)</td>
			<td>리스트에 있는 값 중에서 어느 하나라도 일치하면 된다.</td>
		</tr>
				<tr>
			<td>Like '문자열'</td>
			<td>문자열과 형태가 일치하면 된다. (%: 문자 여러개,_ :문자 하나사용)</td>
		</tr>
		<tr>
			<td>IS NULL</td>
			<td>NULL 값인 경우</td>
		</tr>
			<tr>
			<td rowspan="3">부정 비교 연산자</td>
			<td><>,!=,^=</td>
			<td> 같지 않다</td>
		<tr>
			<td>NOT 칼럼명 = </td>
			<td>~와 같지 않다.</td>
		</tr>
				<tr>
			<td>NOT 칼럼명 ></td>
			<td>~ 보다 크지 않다.</td>
		</tr>
			<tr>
			<td rowspan="3">부정 SQL 연산자</td>
			<td>NOT BETWEEN a AND b</td>
			<td>a와 b의 값 사이에 있으면 안된다. (a,b 포함)</td>
		</tr>
		<tr>
			<td>NOT IN(list)</td>
			<td>리스트에 있는 값 중에서 어느 하나라도 일치하면 안된다.</td>
		<tr>
			<td>IS NOT NULL</td>
			<td>NULL 값이 아닌 경우</td>
		</tr>
	</tbody>
	</table>
	<p>연산자의 우선 순위</p>
<ul>
	<li>1 : 괄호 ()</li>
	<li>2 : NOT 연산자</li>
	<li>3 : 비교연산자, SQL 비교 연산자</li>
	<li>4 : AND</li>
	<li>5 : OR</li>	
</ul>

<h4>ROWNUM,TOP</h4>
<p>ROWNUM :  select 출력시 원하는 만큼만 가져옴 </p>
<p>한건만 가져오고 싶을 때</p>
<ul>
	<li>SELECT * from EMP WHERE ROWNUM = 1</li>
	<li>SELECT * from EMP WHERE ROWNUM < 2</li>
	<li>SELECT * from EMP WHERE ROWNUM <= 1</li>
</ul>
<p>TOP :  select 출력되는 행의 수를 제한함 (syntax) :  TOP (Expression) [PERCENT][WITH TIES] </p>
<ul>
	<li>Expression : 반환할 행의 수를 지정하는 숫자임</li>
	<li>PERCENT : 쿼리 결과 집합에서 처음 Expression%의 행만 반환 됨을 알 수 있음</li>
	<li>WITH TIES :  ORDER BY절이 지정된 경우에만 사용 가능하며, TOP N(PERCENT)의 마지막 행과 같은 값이 있는 경우 추가 행이 출력 되도록 지정 할수 있음.</li>
</ul>
<ul>
	<li>한건만 가져오고 싶을 때 : SELECT TOP(1) * from EMP</li>
	<li>N건만 가져오고 싶을 때 : SELECT TOP(N) * from EMP</li>
</ul>
<h4>SQL 연산자 예시</h4>
<ul>
	<li>IN (list) 연산자 : SELECT * from EMP where (JOB,DEPTNO) IN (('MANAGER',20),('CLERK',30)),SELECT * from EMP where JOB IN (('MANAGER','CLERK') AND DEPTNO IN (20,30)) -- 사원 테이블에서 JOB이 CLERK이면서 30번 부서에 속하거나 JOB이 MANAGER이면서 20번에 속하는 사람 찿아서 출력 </li>
	<li>BETWEEN a AND b : SELECT * from EMP WHERE HEIGHT BETWEEN 170 AND 180; :  키가 170-180 사이에 있는 직원 출력 </li>
	<li>NULL : SELECT * from EMP WHERE HEIGHT IS NULL (* HEIGHT= NULL 하면 대가리깨져도 안뜸) :  키가 NULL인  직원 출력 </li>
	<li> <> : SELECT * from EMP WHERE POSITION <> 'CIA'; : POSITIOn이 CIA가 아닌 직원 출력 </li>
</ul>

<h2>함수</h2>
<ul>
	<li><a href="#dan1hangfunc">단일행 함수</a></li><li></li>
<li></li>
	</ul>
<h3 id="dan1hangfunc">단일행 함수</h3>
<p>특징</p>
<ul>
	<li>SELECT,Where, order by절에 사용 가능하다.</li>
	<li>각 행들에 대해 개별적으로 작용하여 데이터 값들을 조작하고, 각각의 행에 대한 조작 결과를 리턴한다.</li>
	<li>여러 인자를 입력해도 단 하나의 결과만 나온다.</li>
	<li>함수의 인자로 상수,변수 표현식이 사용 가능하고, 하나의 인수를 가지는 경우도 있지만, 여러개의 인수를 가질 수도 있다.</li>
	<li>특별한 경우가 아니면 함수의 인자로 함수를 사용하는 충첩이 가능하다.</li>
</ul>
<p>syntax : 함수명 (칼럼이나 표현식, [arg1,arg2, ...]) </p>
<ul>
	<li><a href="#str1func">문자형 함수</a> : 문자를 입력하면 문자나 숫자 값을 반환한다. ex(LOWER, UPPER, SUBSTR/SUBSTRING, LENGTH/LEN, LTRIM, RTRIM, TRIM)</li>
	<li><a href="#num1func">숫자형 함수</a> : 숫자를 입력하면 문자나 숫자 값을 반환한다. ex(ABS, MOD, ROUND, TRUNC,SIGN, CHR/CHAR, CEIL, FLOOR, POWER 등 )</li>
	<li><a href="#date1func">날자형 함수</a> : DATA 타입의 값을 연산한다. ex(SYSDATE/GETDATE, EXTRACT/DATEPART, TO_NUMBER(TO_CHAR(d,'YYYY'|'MM'|'DD'))/ YEAR|MONTH|DAY)</li>
	<li><a href="#con1func">변환형 함수</a> : 문자, 숫자, 날짜형 값의 데이터를 변환한다. ex(TO_NUMBER, TO_CHAR, TO_DATE/CAST, CONVERY 등 )</li>
	<li><a href="#null1func">NULL 관련 함수</a> : NULL을 처리하기 위한 함수 ex(NVL/ISNULL, NULLIF, COALESCE )</li>
</ul>
<h3 id="str1func">문자형 함수</h3>
<h3 id="num1func">숫자형 함수</h3>
<h3 id="date1func">날자형 함수</h3>
<h3 id="con1func">변환형 함수</h3>
<h3 id="null1func">NULL 관련함수</h3>

</div>

<div id="ddl">
<h3>DDL</h3>
<ul>
	<li>ADD (syntax)- ALTER TABLE tablename  ADD 컬럼명 데이터 유형  : 테이블에 새로운 컬럼 명 추가</li>
	<li>DROP (syntax)- ALTER TABLE tablename  DROP 컬럼명  : 테이블에  컬럼 명 제거</li>
	<li>MODIFY (syntax)- ALTER TABLE tablename  MODIFY (컬럼명 데이터유형 [DEFAULT 식][NOT NULL], 컬럼명2 데이터유형...);  : 테이블에  컬럼명에 대해서 제약조건 등에 대한 변경</li>
	<li>RENAME (syntax)- ALTER TABLE tablename  RENAME 컬럼명 TO  새로운 컬럼명;  : 테이블에  컬럼명에 대해서 새로운 컬럼명으로 변경</li>
	<li>DROP CONSTRAINT (syntax)- ALTER TABLE tablename  DROP CONSTRAINT 제약조건명;  : 테이블에  제약조건명에 대해서 제거</li>
	<li>ADD CONSTRAINT (syntax)- ALTER TABLE tablename  ADD CONSTRAINT 제약조건명 제약조건(컬럼명);  : 테이블에 입력한 제약조건을 가진 제약조건명에 대해서 입력한 컬럼에 대해 추가함</li>
	<li>DROP TABLE(syntax)- DROP 테이블명  : 해당 테이블 제거</li>
	<li>TRUNCATE TABLE (syntax)- ALTER TABLE tablename  DROP 컬럼명  : 테이블에 있는 모든 행들을 제거 테이블과 컬럼들은 남겨둠</li>
</ul>


</div>

<div id="dcl">
<h3>DCL</h3>



</div>


<div id="tcl">
<h3>TCL : 트랜잭션 컨트롤 언어</h3>
<p>트랜잭션의 정의 : 트랜잭션은 데이터베이스의 논리적 연산 단위로 밀접히 관련되어 분리될 수 없는 한개 이상의 데이터베이스 조작을 의미함. 즉 하나의 트랜잭션에는 하나이상의 sql문이 포함된다. </p>
<p>트랜잭션은 데이터베이스의 논리적 연산 단위로 밀접히 관련되어 분리될 수 없는 한개 이상의 데이터베이스 조작을 의미함. 즉 하나의 트랜잭션에는 하나이상의 sql문이 포함된다. </p>
<h3>트랜잭션의 특성</h3>
<ul>
	<li>원자성(atomicity) : 트랜잭션에서 정의된 연산들은 모두 성공적으로 실행되던지 아니면 전혀 실행되지 않은 상태로 남아있어야 한다.</li>
	<li>일관성(consistency) : 트랜잭션이 실행되기 전의 데이터베이스 내용이 잘못되어 있지 않으면, 트랜잭션이 실행된 이후에도 데이터베이스의 내용에 잘못이 있으면 안된다.</li>
	<li>고립성(isolation) : 트랜잭션이 실행되는 도중에 다른 트랜잭션의 영향을 받아 잘못된 결과를 만들어서는 안된다.</li>
	<li>지속성(durability) : 트랜잭션이 성공적으로 수행되면 그 트랜잭션이 갱신한 데이터베이스의 내용은 영구적으로 저장된다.</li>
</ul>

<ul>
	<li>COMMIT : 올바르게 반영된 데이터를 데이터베이스에 반영 시킴.</li>
	<li>ROLLBACK : 트랜잭션 시작 이전의 상태로 돌림</li>
	<li>SAVEPOINT : 저장점 기능을 함.</li>
</ul>

<h3>COMMIT</h3>
<p>입력한 자료나 수정한 자료에 대해서 혹은 삭제한 것에 대해서 전혀 문제가 없다고 판단할 시에, 해당 명령어를 사용하여 트랜잭션을 완료할 수 있음. </p>
<p>INSERT,UPDATE, DELETE 등 DML 명령어 후에 변경 작업이 완료 되었음을 디비에 알려주기 위해 사용한다. </p>
<h4>특징</h4>
<ul>
	<li>단지 메모리 버퍼에만 영향을 받았기 때문에 데이터 변경 이전의 상태로 복구 가능함.</li>
	<li>현재 사용자는 select 문장으로 결과 확인이 가능하다.</li>
	<li>다른 사용자는 현재 사용자가 수행한 명령의 결과를 볼 수 없다.</li>
	<li>변경 된 행은 잠금(LOCKING)이 설정되어서 다른 사용자가 변경 할 수 없다.</li>
</ul>

<p>SQL 서버에서 트린잭션은 다음의 3가지 방식으로 이루어짐 </p>

<ul>
	<li>AUTO COMMIT : sql 서버의 기본 방식이며, DML, DDL을 수행할 때마다, DBMS가 트랜잭션을 컨트롤하는 방식이다. 명령어가 성공적으로 수행되면, 자동으로 COMMIT을 수행하고 오류가 발생하면 ROLLBACK을 수행한다.</li>
	<li>암시적 트랜잭션 : 오라클에서 사용하는 방법이며, DBMS로 처리하고 트랜잭션 끝에는 사용자가 COMMIT, ROLLBACK을 직접 타이핑해서 처리하는 방법이다.</li>
	<li>명시적 트랜잭션 : 트랜잭션과 끝을 모두 사용자가 지정하는 방식임. BEGIN TRANSACTION으로 트랜잭션을 시작하고 COMMIT TRANSACTION 혹은 ROLLBACK TRANSACTION으로 트랜잭션을 종료한다. ROLLBACK만다면 최초의 BEGIN시점까지 날아감.</li>
</ul>

<h3>ROLLBACK</h3>
<p>데이터 변경사항이 취소되어, 변경전으로 돌아감 </p>
<ul>
	<li>데이터에 대한 변경 사항은 취소된다.</li>
	<li>이전 데이터가 재 저장된다.</li>
	<li>관련된 행에 대해 잠금이 풀리고, 다른 사용자들이 행을 조작 할 수 있게 된다.</li>
</ul>
<h4>COMMIT과 ROLLBACK으로 얻을수 있는 효과</h4>
<ul>
	<li>데이터 무결성 보장</li>
	<li>영구적인 변경을 하기 전에 데이터의 변경 사항 확인 가능</li>
	<li>논리적으로 ㅇ녀관된 작업을 그룹핑하여 처리 가능</li>
</ul>
<h3>SAVEPOINT</h3>
<p>저장점을 정의하여 롤백할때 해당 시점으로 돌아가는게 가능하도록 함</p>
<p>SAVEPOINT (syntax) - SAVEPINT svpt1 :  현재 시점을 svpt1으로 저장함</p>
<p>이렇게 저장된 세이브 포인트는 롤백등으로 ROLLBACK TO svpt1으로 사용되어 질 수 있다.</p>
<p>sql server의 경우 SAVE TRANSACTION svtp1,ROLLBACK TRANSACTION svpt1 으로 가능</p>
<ul>
	<li>데이터에 대한 변경 사항은 취소된다.</li>
	<li>이전 데이터가 재 저장된다.</li>
	<li>관련된 행에 대해 잠금이 풀리고, 다른 사용자들이 행을 조작 할 수 있게 된다.</li>
</ul>
</div>





























