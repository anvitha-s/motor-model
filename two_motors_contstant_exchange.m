V_amp = 200;
a=0.3;
L=100;
v2_u = 1:V_amp/(a*L):V_amp;
v2_d = V_amp - V_amp/(L*(1-a)):-(V_amp/(L*(1-a))):0;
v2 = [v2_u,v2_d];
v2_t = [v2,v2,v2,v2,v2,v2,v2,v2,v2,v2];
x(1:10000) = 0;
x2(1:10000) = 0;
for i=1:10000
    if i==1
        [index,incr] = increment(i,450);
        x(i) = 450 + (incr*dt + sqrt(2*dt)*randn(1,1));
        [index,incr] = increment(i,490);
        x2(i) = 490 + (incr*dt + sqrt(2*dt)*randn(1,1));
    else
        [index,incr] = increment(i,x(i-1));
        x(i) = x(i-1) + (incr*dt + sqrt(2*dt)*randn(1,1));
        [index,incr] = increment(i,x2(i-1));
        x2(i) = x2(i-1) + (incr*dt + sqrt(2*dt)*randn(1,1));
        r = x2(i-1) - x(i-1);
        if abs(r) < 1
            rep_force = 1e8/r^6;
            x2(i) = x2(i) + 0.5*sign(r)*rep_force*dt^2;
            x(i) = x(i) - 0.5*sign(r)*rep_force*dt^2;
        end
    end
        if(x(i) > 1000 | x(i) < 0)
        disp('exiting loop');
        break;
        end
end
disp(x);
plot(x,0.001:0.001:10,x2,0.001:0.001:10);
plot(1:1:1000,v2_t);