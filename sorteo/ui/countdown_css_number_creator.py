template = """
.cd-number-%(name)s {
	position: absolute;
	opacity: 0;
	margin: 0 auto 0 auto;
	-webkit-animation: cd-number-six-anim 1.2s ease %(interval)ss 1 normal;
	-moz-animation: cd-number-six-anim 1.2s ease %(interval)ss 1 normal;
	-ms-animation: cd-number-six-anim 1.2s ease %(interval)ss 1 normal;
	-o-animation: cd-number-six-anim 1.2s ease %(interval)ss 1 normal;
	animation: cd-number-six-anim 1.2s ease %(interval)ss 1 normal;
}

@-webkit-keyframes cd-number-six-anim {
	from {-webkit-transform: scale(0.1); opacity: 0;}
	to {  -webkit-transform: scale(0.6); opacity: 1;}}
	
@-moz-keyframes cd-number-six-anim {
	from {-moz-transform: scale(0.1); opacity: 0;}
	to {  -moz-transform: scale(0.6); opacity: 1;}}
	
@-o-keyframes cd-number-six-anim {
	from {-o-transform: scale(0.1); opacity: 0;}
	to {  -o-transform: scale(0.6); opacity: 1;}}
	
@-ms-keyframes cd-number-six-anim {
	from {-ms-transform: scale(0.1); opacity: 0;}
	to {  -ms-transform: scale(0.6); opacity: 1;}}
	
@keyframes cd-number-six-anim {
	from {transform: scale(0.1); opacity: 0;}
	to {  transform: scale(0.6); opacity: 1;}}
"""



number_names = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirdteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
number_names.reverse()
interval_delta = 1.2
interval_value = 0


for number in number_names:
	print template % {'name':number, 'interval': interval_value}
	interval_value += interval_delta
	print 
	print 

