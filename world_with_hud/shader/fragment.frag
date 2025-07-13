// Fragment Shader
#version 410 core
precision highp float;
uniform sampler2D u_texture;
uniform int u_mode_f;
uniform vec3 u_color;
out vec4 o_color;

void main() {
    if (u_mode_f == 0 || u_mode_f == 2) {
        o_color = texture(u_texture, p_texcoord);
    } else {
        o_color = vec4(u_color, 1.0);
    }
}