(this.webpackJsonpgiantgraph=this.webpackJsonpgiantgraph||[]).push([[0],{35:function(e,t,n){},36:function(e,t,n){},49:function(e,t,n){},50:function(e){e.exports=JSON.parse('[{"name":"Afghanistan","code":"AF"},{"name":"China","code":"CH"}]')},62:function(e,t,n){},63:function(e,t,n){"use strict";n.r(t);var a=n(1),o=n.n(a),i=n(23),s=n.n(i),r=(n(35),n(3)),c=n(4),l=n(8),u=n(6),d=n(7),h=(n(36),function(e){Object(u.a)(n,e);var t=Object(d.a)(n);function n(){return Object(r.a)(this,n),t.apply(this,arguments)}return Object(c.a)(n,[{key:"render",value:function(){return this.props.open?o.a.createElement("div",{id:"SideTab"},o.a.createElement("button",{className:"btn close-btn",onClick:this.props.closeSide},"\xd7"),o.a.createElement("h1",{id:"info-title"},this.props.node.name),o.a.createElement("hr",null),o.a.createElement("p",{id:"main-info"},this.props.node.description),o.a.createElement("p",null,o.a.createElement("a",{href:this.props.node.href,target:"_blank",rel:"noreferrer",id:"wiki-link"},"Read More"))):null}}]),n}(o.a.Component)),f=n(24),g=n.n(f),p=(n(49),n(50)),m=function(e){var t=e.trim().toLowerCase(),n=t.length;return 0===n?[]:p.filter((function(e){return e.name.toLowerCase().slice(0,n)===t}))},S=function(e){Object(u.a)(n,e);var t=Object(d.a)(n);function n(){var e;return Object(r.a)(this,n),(e=t.call(this)).onSubmit=function(t){console.log(t),"Enter"==t.keyCode&&(e.props.setSearchTerm(e.state.value),console.log(e.state.value))},e.onChange=function(t,n){var a=n.newValue;e.setState({value:a})},e.onSuggestionsFetchRequested=function(t){var n=t.value;e.setState({suggestions:m(n)})},e.onSuggestionsClearRequested=function(){e.setState({suggestions:[]})},e.state={value:"",suggestions:[]},e}return Object(c.a)(n,[{key:"render",value:function(){var e=this.state,t=e.value,n=e.suggestions;return o.a.createElement(g.a,{suggestions:n,onSuggestionsFetchRequested:this.onSuggestionsFetchRequested,onSuggestionsClearRequested:this.onSuggestionsClearRequested,getSuggestionValue:function(e){return e.name},renderSuggestion:function(e){return o.a.createElement("div",null,e.name)},inputProps:{placeholder:"Search",value:t,onChange:this.onChange.bind(this),onkeydown:this.onSubmit}})}}]),n}(o.a.Component),v=n(5),b=n(28),k=function(e){Object(u.a)(n,e);var t=Object(d.a)(n);function n(e){var a;return Object(r.a)(this,n),(a=t.call(this,e)).fetchData=function(e){fetch("/see?search="+e).then((function(e){return console.log(e.data)})).then((function(e){return e.json()})).then((function(e){a.setState({isLoaded:!0,data:e.data})}))},a.fgRef=o.a.createRef(),a.state={selectedNode:"",hoverNode:"",visited:new Set,highlightLinks:new Set,data:{},isLoaded:!1},a}return Object(c.a)(n,[{key:"render",value:function(){var e=this;return o.a.createElement(b.a,{ref:this.fgRef,graphData:this.fetchData(this.props.searchTerm),enableNodeDrag:!1,nodeLabel:"href",nodeCanvasObject:function(t,n,a){var o=Math.max(300*t.value/a,2);n.font="".concat(o,"px Times-new-roman"),t.val=o,n.textAlign="center",n.textBaseline="middle",e.props.node&&e.props.node.id===t.id?n.fillStyle="#0000FF":e.state.hoverNode===t||e.state.visited.has(t.id)?n.fillStyle="#751F80":n.fillStyle="#0645BD",n.fillText(t.name,t.x,t.y)},onNodeHover:function(t){t?(document.body.style.cursor="pointer",e.setState({hoverNode:t})):(document.body.style.cursor="default",e.setState({hoverNode:null}))},onNodeClick:function(t){if(t){e.props.setNode(t),e.props.openSide();var n,a=new Set,o=Object(v.a)(e.props.data.links);try{for(o.s();!(n=o.n()).done;){var i=n.value;i.source.id!==t.id&&i.target.id!==t.id||a.add(i)}}catch(s){o.e(s)}finally{o.f()}e.setState({highlightLinks:a}),e.setState({visited:e.state.visited.add(t.id)}),e.fgRef.current.centerAt(t.x-40,t.y,1e3),e.fgRef.current.zoom(5,2e3)}},onBackgroundClick:function(){e.setState({highlightLinks:new Set})},linkWidth:function(t){return e.state.highlightLinks.has(t)?5:1},cooldownTicks:50,onEngineStop:function(){return e.fgRef.current.zoomToFit(400)}})}}]),n}(o.a.Component),j=(n(62),function(e){Object(u.a)(n,e);var t=Object(d.a)(n);function n(e){var a;return Object(r.a)(this,n),(a=t.call(this,e)).setSearchTerm=function(e){a.setState({searchTerm:e})},a.state={open:!1,node:null,searchTerm:""},a.openSide=a.openSide.bind(Object(l.a)(a)),a.closeSide=a.closeSide.bind(Object(l.a)(a)),a.setNode=a.setNode.bind(Object(l.a)(a)),a}return Object(c.a)(n,[{key:"openSide",value:function(){this.setState({open:!0})}},{key:"closeSide",value:function(){this.setState({open:!1})}},{key:"setNode",value:function(e){this.setState({node:e})}},{key:"render",value:function(){return o.a.createElement("div",{className:"row"},o.a.createElement("div",{className:"col-md-4",id:"sidebar"},o.a.createElement(S,null),o.a.createElement(h,{open:this.state.open,closeSide:this.closeSide,node:this.state.node})),o.a.createElement("div",{className:"col-lg",id:"graph"},o.a.createElement(k,{searchTerm:this.state.searchTerm,node:this.state.node,setNode:this.setNode,openSide:this.openSide,closeSide:this.closeSide})))}}]),n}(o.a.Component));s.a.render(o.a.createElement(j,null),document.getElementById("root"))}},[[63,1,2]]]);
//# sourceMappingURL=main.770c2ab5.chunk.js.map