/*
자바스크립트의 함수는 function = 파이썬의 def
*/

/*
function add(x , y) {
    return x + y;
}
*/

/* 반복분 */
/*
[1] i=i+1
[2] i+=1
[3] i++
[4] ++i

독자적으로 쓰면 [3] , [4] 는 차이가 없지만 다른 연산자와 사용될 경우 차이가 있음
[4] 은 더한 후에 연산을 하라는 것이고 , [3] 는 연산 후에 더하라는 것임
*/

/*
console.log("1 부터 10 까지 출력하기")

a = 5;
b = ++a;    // = , ++ : 전치연산자라고 하며 무엇보다 연산우선순위가 높음
console.log(`a=${a} b=${b}`);

a = 5;
b = a++;
console.log(`a=${a} b=${b}`);


// for( 변수 초기값 , 조건식 , 증갑치 ) {}
// 조건식의 True 일때만 동작함
for( i = 1 ; i <= 10 ; i++ ) {
    console.log(`i = ${i}`)
}

for( i = 10 ; i > 0 ; i-- ) {
    console.log(`i = ${i}`)
}

k = 1

for( i = 1; i <= 10; i++ ){
    console.log(`k=${k}`);
    k += 2;
}

let arr = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ];
console.log(arr);
// 인덱싱은 지원하지만 슬라이싱은 사용 불가

for( i = 0; i<arr.length; i++){
    console.log(arr[i]);
}

// 배열에 데이터 추가
arr.push(11);
console.log(arr);

// in 연산자 : 배열로부터 항목을 하나씩 가져옴
for(i in arr){
    console.log(`i=${i} arr[i]=${arr[i]}`);
}

// of 연산자 : 배열로부터 항목을 하나씩 가져옴 , 배열 요소를 하나씩 가져온다.
for(i of arr){
    console.log(`i=${i}`);
}
*/

/*
words = [ "rain" , "umbrellar" , "desk" , "note" , "assembly" , "marble" , "subway" , "flower" , "cloud" , "hospital" , "hammer" , "murder" ];
for(i = 0; i < words.length; i++) {
    console.log(words[i]);
}

for( i in words ) {
    console.log(words[i]);
}

for( w of words ) {
    console.log(w);
}

// 파이썬의 람다 == 화살표 함수
words.forEach(element => {
    console.log(element);
});
*/

/*
// 파이썬의 dict (키와 값 쌍으로 저장하는 것)
// 자바 스크립트에서는 json 이라고 함
let person = {"name" : "홍길동" , age:23 , phone:"010-0000-0001"};
console.log(person.name);
console.log(person.age);
console.log(person.phone);

console.log(person["name"]);
console.log(person["age"]);
console.log(person["phone"]);

// json 객체 배열
let persons = [
    {name:"홍길동" , phone:"010-0000-0001"} ,
    {name:"임꺽정" , phone:"010-0000-0002"} ,
    {name:"장길산" , phone:"010-0000-0003"} ,
    {name:"강감찬" , phone:"010-0000-0004"} ,
    {name:"서희"   , phone:"010-0000-0005"}
];

for(i=0; i<persons.length; i++) {
    console.log(`${persons[i].name} ${persons[i].phone}`);
}

for(i in persons) {
    console.log(`${persons[i].name} ${persons[i].phone}`);
}

for(p of persons) {
    console.log(`${p.name} ${p.phone}`);
}

persons.forEach(p => {
    console.log(`${p.name} ${p.phone}`);
})
*/

// 함수
// 파이썬에서의 함수 : def
// 자바스크립트에서의 함수
/*
function 함수명(매개변수){ 
    return ;
}
*/

/*
function add(x , y) {
    return x + y;
}

// 1 부터 N 까지 더하는 함수
function sigma(limit=10) {
    sum = 0;
    for(i = 1; i <= limit; i++) {
        sum += i;
    }

    return sum;
}

console.log(add(4,6));
console.log(sigma(100));
*/

// 함수 표현식
// 함수 : 미리 만들고 프로그램이 종료할 때까지 메모리를 계속해서 차지하고 있음
// 일시적인 함수 : 파이썬에서는 람다 , 자바스크립트에서는 화살표함수
// 함수 표현식에서는 함수에 이름이 없고 매개변수만 줌
/*
let myFunc = function(매개변수) {
    return ;
}
*/

// 주로 이벤트 핸들러(마우스 왼쪽 눌렀을 때 호출되는 함수) 를 만들때 함수표현식으로 함수를 만듬
/*
add = function(x , y) {
    return x + y;
}
*/
/*
add = (x,y) => x+y;
*/

/*
add2 = function(x,y) {
    return x + y;
}

add3 = (x,y) => x+y;

console.log(add2(10,20))
console.log(add3(10,20))

// 검색
// 화살표 함수(람다) , 화살표 함수는 this 를 사용할 수 없음(파이썬에서의 self 와 같은 역할)
let arr = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10];
let result = arr.filter((a) => a % 2 == 0);

console.log(result);
*/

/*
let arr = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10];

words = [ "rain" , "umbrellar" , "desk" , "note" , "assembly" , "marble" , "subway" , "flower" , "cloud" , "hospital" , "hammer" , "murder" ];

let persons = [
    {name:"홍길동" , phone:"010-0000-0001"} ,
    {name:"임꺽정" , phone:"010-0000-0002"} ,
    {name:"장길산" , phone:"010-0000-0003"} ,
    {name:"강감찬" , phone:"010-0000-0004"} ,
    {name:"서희"   , phone:"010-0000-0005"}
];

result = words.filter( w => w.length >= 5 );
console.log(result);

// 문제 1. arr 배열에서 3 의 배수 찾아내기
result1 = arr.filter( n => n % 3 == 0 );
console.log(result1)

// 문제 2. arr 배열에서 5 보다 큰 수 찾아내기
result2 = arr.filter( n => n > 5 );
console.log(result2)

// 문제 3. words 에서 'a' 가 들어간 단어 찾아내기
result3 = words.filter( w => w.includes("a"));
console.log(result3)

// 문제 4. words 에서 'h' 나 'r' 로 시작하는 단어만 찾아내기
result4 = words.filter( w => w[0] === "h" || w[0] === "r");
console.log(result4)

// 문제 5. persons 배열에서 전화번호가 010-0000-0002 인 사람의 이름 찾아내기
result5 = persons.filter( p => p.phone == "010-0000-0002" );
if (result5.length > 0) {
    result5.forEach( e => {
        console.log(e.name , e.phone);
    })
}

// 문제 6. persons 배열에서 임꺽정인 사람의 전화번호
result6 = persons.filter( p => p.name == "임꺽정" ).forEach(e => console.log(e.name , e.phone));

// 문제 7. persons 배열에서 임꺽정과 서희의 전화번호
result7 = persons.filter( p => p.name == "서희" || p.name == "임꺽정").forEach(e => console.log(e.name , e.phone));
*/

// let 변수와 var 변수의 차이점
// var : 자바스크립트가 인터프리터 언어라서 굳이 변수 선언을 하지 않아도 됨. 변수 선언을 하려면 var 를 사용했었음


/*
// var 변수 선언을 나중에 해도 문제 없이 작동함
a = 10;
var a; // 나중에 변수 선언을 함
console.log(a);
*/

/*
// let 변수는 나중에 선언을 하면 문제가 발생됨
b = 5;
let b;
console.log(b);
*/

/*
// 호이스팅
// 원래 {} 안에 있는 변수는 {} 안에서만 사용되어야하는데 기존에 있는 동일명의 변수를 가져가서 사용함 = 호이스팅
message = "Hello";
if (true){
    var message = "안녕하세요.";
}

console.log(message);

// let 의 경우
message2 = "Hello";
if (true){
    let message2 = "안녕하세요.";
}

console.log(message2);
*/