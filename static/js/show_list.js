class showList{
    constructor(){
        this.data = this.getdata();
        console.log(this.data);
    }

    getdata(){
        fetch('http://127.0.0.1:8000/question/list').then((response)=>{
            return response.json();
        })
    }
}

window.onload = ()=>{
    new showList()
}