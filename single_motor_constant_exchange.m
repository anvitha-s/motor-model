V_amp = 200;
a=0.3;
dt=0.001;
L=100;
v2_u = 1:V_amp/(a*L):V_amp;
v2_d = V_amp - V_amp/(L*(1-a)):-(V_amp/(L*(1-a))):0;
v2 = [v2_u,v2_d];
v2_t = [v2,v2,v2,v2,v2,v2,v2,v2,v2,v2];
xp=1:1:1000;
x(1:10000) = 0;
for i=1:10000
    if i==1
        [index,incr] = increment(i,450);
        x(i) = 450 + (incr*dt + sqrt(2*dt)*randn(1,1));
       
    else
        [index,incr] = increment(i,x(i-1));
        x(i) = x(i-1) + (incr*dt + sqrt(2*dt)*randn(1,1));
         if (index== 1)
            %disp(incr);
            %disp(x(i) -x(i-1));
        end
    end
        if(x(i) > 1000 | x(i) < 0)
        disp('exiting loop');
        break;
        end
    %disp(i);    
    %figure
    %subplot(2,1,1);
    %plot(xp,v1);
    %if(index == 0 )
    %    hold on
    %    plot(x,0,'o');
    %end
    %subplot(2,1,2);
    %plot(xp,v2_t);
    %if( index == 1)
    %    hold on 
    %    plot(x,0,'o');
    %end
end
disp(x);