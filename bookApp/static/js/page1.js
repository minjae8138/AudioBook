//파일 이름 가져오기
const filename = document.getElementById('fileName')

document.getElementById('files').addEventListener('change', function(){
	if(this.files[0] == undefined){
		filename.innerText = '선택된 파일없음';
		return;
	}
	filename.innerText = this.files[0].name;
});







//function LoadingWithMask() {
//    //화면의 높이와 너비를 구합니다.
//    var maskHeight = $(document).height();
//    var maskWidth  = window.document.body.clientWidth;
//
//    //화면에 출력할 마스크를 설정해줍니다.
//    var mask       ="<div id='mask' style='position:absolute; z-index:9000; background-color:#000000; display:none; left:0; top:0;'></div>";
//    var loadingImg ='';
//
//    loadingImg +="<div id='loadingImg'>";
//    loadingImg +=" <img src={% static 'src/rio4.png'%} style='position: relative; display: block; margin: 0px auto;'/>";
//    loadingImg +="</div>";
//
//    //화면에 레이어 추가
//    $('body')
//        .append(mask)
//        .append(loadingImg)
//
//    //마스크의 높이와 너비를 화면 것으로 만들어 전체 화면을 채웁니다.
//    $('#mask').css({
//            'width' : maskWidth
//            ,'height': maskHeight
//            ,'opacity' :'0.3'
//    });
//
//    //마스크 표시
//    $('#mask').show();
//
//    //로딩중 이미지 표시
//    $('#loadingImg').show();
//}

