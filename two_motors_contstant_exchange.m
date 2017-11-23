%V_amp = 200;
%length of one sawtooth
%L=100;
%coefficient in repulsion equation
cI=1e4;
%time step
dt=0.001;
%positions of molecular motors at n*dt
x1(1:10000) = 0;
x2(1:10000) = 0;
for i=1:10000
    if i==1
        %initial time step,  x(0) = 450
        [index,incr] = increment(i,450);
        x1(i) = 450 + (incr*dt + sqrt(2*dt)*randn(1,1));
        [index,incr] = increment(i,490);
        x2(i) = 490 + (incr*dt + sqrt(2*dt)*randn(1,1));
    else
        %index - index of potential field - v1(flat) or v2
        %incr - component of time derivative of x due to potential field
        [index,incr] = increment(i,x1(i-1));
        %x for next time step 
        %sqrt(2*dt)*randn(1,1) - change in x due to diffusion
        x1(i) = x1(i-1) + (incr*dt + sqrt(2*dt)*randn(1,1));
        %similar computation for 2nd motor with x coordinate x2
        [index,incr] = increment(i,x2(i-1));
        x2(i) = x2(i-1) + (incr*dt + sqrt(2*dt)*randn(1,1));
        % r - distance between the two motors in the last time step
        r = x2(i-1) - x1(i-1);
        % diameter of both motors taken as 1 unit 
        if abs(r) < 1
            %motors are in contact at x(i-1)
            %rep_force - repulsion force/unit mass
            rep_force = cI/r^6;
            % adding effect of repulsion
            x2(i) = x2(i) + 0.5*sign(r)*rep_force*dt^2;
            x1(i) = x1(i) - 0.5*sign(r)*rep_force*dt^2;
        end
    end
    %if motor moves out of frame
        if(x1(i) > 1000 | x1(i) < 0 | x2(i) > 1000 | x2(i) < 0)
        disp('exiting loop');
        break;
        end
end
disp(x1);
plot(x1,0.001:0.001:10,x2,0.001:0.001:10);